from django.http import JsonResponse
from django.shortcuts import redirect, render
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.contrib.auth import authenticate
from rest_framework.response import Response

from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.db.models import Q
from .serializers import RegisterSerial,LoginSerial,UserSerial
from django.views import View

from .models import Publisher,Author,Book
from .forms import PublishForm,BookForm,AuthorForm
# Create your views here.
def author_page(request):
    """Display the author form page"""
    return render(request, "author.html")

def publisher_page(request):
    """Display the publisher form page"""
    return render(request, "Publisher.html")

def book_page(request):
    """Display the book form page"""
    return render(request, "book.html")
def home(request):
    return render(request, "home.html")

def login_page(request):
    return render(request, "login.html")
@method_decorator(csrf_exempt, name="dispatch")
class AuthorView(View):
    def post(self, request):
        try:
            form_data = json.loads(request.body)
            form = AuthorForm(form_data)
            
            if form.is_valid():
                author = form.save()
                return JsonResponse({
                    "success": True,
                    "message": "Author saved successfully!",
                    "data": {
                        "id": author.id,
                        "name": str(author),
                        "email": author.email
                    }
                })
            else:
                return JsonResponse({
                    "success": False,
                    "errors": form.errors
                }, status=400)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=500)
                
    def get(self,request):
        
            query = request.GET.get("q","")
            if len(query)<3:
                return JsonResponse([], safe=False)
            else:
                pref_res = Author.objects.filter(Q(fname__istartswith=query) | Q(lname__istartswith=query))
                gen_ans = Author.objects.filter(Q(fname__icontains=query) | Q(lname__icontains=query)).exclude(
            Q(fname__istartswith=query) | Q(lname__istartswith=query)
            )
                res= list(pref_res)+list(gen_ans)
            data=[]
            for a in res:
                data.append({
                    "name":str(a),
                    "email":a.email
                })
            return JsonResponse(data,safe=False)
@method_decorator(csrf_exempt, name="dispatch")
class PublisherView(View):

    def post(self, request):
        try:
            form_data = json.loads(request.body)
            form = PublishForm(form_data)
            
            if form.is_valid():
                publisher = form.save()
                return JsonResponse({
                    "success": True,
                    "message": "Publisher saved successfully!",
                    "data": {
                        "id": publisher.id,
                        "name": publisher.name,
                        "country": publisher.country,
                        "website": publisher.website
                    }
                })
            else:
                return JsonResponse({
                    "success": False,
                    "errors": form.errors
                }, status=400)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=500)
                
    def get(self,request):
        
            query = request.GET.get("q","")
            if len(query)<3:
                return render(request, "publisher.html")
            else:
                pref_res = Publisher.objects.filter(name__icontains=query)
                data=[]
                for p in pref_res:
                     data.append({
                          "name":p.name
                     })
                return JsonResponse(data,safe=False)

@method_decorator(csrf_exempt, name="dispatch")
class BookDataView(View):
    """Returns all authors and publishers for book form dropdowns"""
    def get(self, request):
        authors = Author.objects.all()
        publishers = Publisher.objects.all()
        
        data = {
            "author": [
                {"id": a.id, "fname": a.fname, "lname": a.lname}
                for a in authors
            ],
            "publisher": [
                {"id": p.id, "name": p.name}
                for p in publishers
            ]
        }
        return JsonResponse(data, safe=False)

@method_decorator(csrf_exempt, name="dispatch")           
class BookView(View):
    def post(self, request):
        try:
            form_data = json.loads(request.body)
            form = BookForm(form_data)
            
            if form.is_valid():
                book = form.save()
                return JsonResponse({
                    "success": True,
                    "message": "Book saved successfully!",
                    "data": {
                        "id": book.id,
                        "title": book.title,
                        "publisher": book.publisher.name
                    }
                })
            else:
                return JsonResponse({
                    "success": False,
                    "errors": form.errors
                }, status=400)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=500)
            
    def get(self,request):
        
            query=request.GET.get("q","")
            pref_res = Book.objects.filter((Q(author__fname__icontains=query) | Q(author__lname__icontains=query)) | (Q(publisher__name__icontains=query))).distinct()
            data = []

            for b in pref_res:

                authors = ", ".join(
                    [str(a) for a in b.author.all()]
                )

                data.append({
                    "title": b.title,
                    "authors": authors,
                    "publisher": b.publisher.name
                })

            return JsonResponse(data, safe=False)

class Register(generics.CreateAPIView):
     queryset=User.objects.all()
     #permission_classes=(AllowAny,)
     serializer_class= RegisterSerial

class LoginView(generics.GenericAPIView):
     serializer_class=LoginSerial
     def post(self,request,*args,**kwargs):
          username=request.data.get('username')
          password=request.data.get('password')
          user=authenticate(username=username,password=password)
          if user is not None:
               refresh = RefreshToken.for_user(user)
               user_serial=UserSerial(user)
               return Response({
                    'refresh':str(refresh),
                    'access': str(refresh.access_token),
                    'is_admin':user.is_staff,
                    'user': user_serial.data
               })
          else:
               return Response({'detail':'Invalid credentials'}, status=401)
               


        

        
        



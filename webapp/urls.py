from django.urls import path
from .views import AuthorView, PublisherView, BookView, BookDataView

urlpatterns = [

    # AUTHOR
    path("author/make/", AuthorView.as_view()),     # POST
    path("author/search/", AuthorView.as_view()),   # GET

    # PUBLISHER
    path("publisher/make/", PublisherView.as_view()),   # POST
    path("publisher/search/", PublisherView.as_view()), # GET

    # BOOK 
    path("book/search/", BookView.as_view()),
    path("book/make/",BookView.as_view()),
    path("book/data/", BookDataView.as_view()),  # GET - for form dropdowns

]

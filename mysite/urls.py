"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from webapp import views
from django.contrib import admin
from django.urls import include, path
from webapp.views import Register,LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register', Register.as_view(), name="auth_register"),
    path("api/", include("webapp.urls")),
    
  
    path('login/', views.login_page, name="login"),
    path('home/', views.home, name="home"),
    path('author/', views.author_page, name="author_page"),      # NEW
    path('publisher/', views.publisher_page, name="publisher_page"),  # NEW
    path('book/', views.book_page, name="book_page"),            # NEW
    
   
    path('api/auth/login/', LoginView.as_view(), name="auth_login"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
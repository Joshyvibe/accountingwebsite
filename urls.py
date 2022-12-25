from django.contrib import admin
from django.urls import path
from . import views
from acct_app import views as user_view
from django.contrib.auth import views as auth



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('typography/', views.typography, name='typography'),
    path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='acct_app/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),
]

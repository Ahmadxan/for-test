from django.urls import path
from . import views


urlpatterns =[
    path('', views.home_page, name = 'home_page'),
    path('author/list/', views.author_list, name = 'author_list'),
    path('author/create/', views.author_create, name = 'author_create'),
]
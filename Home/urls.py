from django.urls import path
from . import views



urlpatterns = [
    path('',views.home_page, name='Home'),
    path('product/<str:slug>',views.One_pruduct, name='product'),
    path('Category/<str:slug>',views.Categorys_handeling, name='Category'),
]

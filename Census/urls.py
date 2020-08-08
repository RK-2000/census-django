from django.urls import path 
from . import views

urlpatterns = [ 
    path('' , views.index,  name='index'),
    path('home/' , views.index,  name='index'),
    path('sign-up/', views.signup, name='signup'),
    path('logged/',views.logged,name='logged'),
]
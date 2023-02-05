from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('cells', cells, name='cells'),
    path('options', options, name='options'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='homepage'),
    path('Cells', Cells, name='Cells'),
    path('sign-in', signin, name='sign-in'),
    path('form', Form, name='form'),
    path('members', members, name='members'),
]

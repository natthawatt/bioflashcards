from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage

def home(request):
	return render(request, 'home/home.html')
	
def About(request):
	return render(request, 'home/About.html')


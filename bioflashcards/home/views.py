from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home/home.html')

def cells(request):
	return render(request, 'home/cells.html')

def signin(request):
	return render(request, 'home/sign-in.html')

def howtouse(request):
	return render(request, 'home/howtouse.html')

def options(request):
	return render(request, 'home/options.html')



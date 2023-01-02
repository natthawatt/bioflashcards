from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
	return render(request, 'home/home.html')

def Cells(request):
	return render(request, 'home/cells.html')

def signin(request):
	return render(request, 'home/sign-in.html')

def Form(request):
	return render(request, 'home/form.html')

def members(request):
	return render(request, 'home/members.html')
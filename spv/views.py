from django.shortcuts import render

def home(request):
	return render(request, 'home/index.html')

def lugares(request):
	return render(request, 'lugares/index.html')
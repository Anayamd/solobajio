from django.shortcuts import render
from .models import Negocio

def home(request):
	# no_pagaron = Negocio.objects.orderby(ranking)
	return render(request, 'home/index.html')

def lugares(request):
	negocios = Negocio.objects.all()
	return render(request, 'lugares/index.html', {'negocios':negocios})

def eventos(request):
	return render(request, 'eventos/index.html')
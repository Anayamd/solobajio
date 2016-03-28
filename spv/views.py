from django.shortcuts import render, get_object_or_404
from .models import Negocio, Evento

def home(request):
	# no_pagaron = Negocio.objects.orderby(ranking)
	return render(request, 'home/index.html')

def lugares(request):
	negocios = Negocio.objects.all()
	return render(request, 'lugares/index.html', {'negocios':negocios})

def eventos(request):
	eventos = Evento.objects.all()
	return render(request, 'eventos/index.html', {'eventos': eventos})

def info(request, pk):
	negocio = get_object_or_404(Negocio, pk=pk)
	return render(request, 'info/index.html', {'negocio': negocio})
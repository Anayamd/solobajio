from django.shortcuts import render, get_object_or_404
from .models import Negocio, Evento, Industry

def home(request):
	# no_pagaron = Negocio.objects.orderby(ranking)
	return render(request, 'home/index.html')

def lugares(request, search=''):
	negocios = Negocio.objects.all().exclude(published_date__isnull=True).order_by('ranking')
	industries = Industry.objects.all()
	titulo = 'todo'
	
	if request.method == 'POST' and request.POST['filtro'] != 'todo':
		_filtro = request.POST['filtro']
		negocios = negocios.filter(industry__ind_type__contains=_filtro)
		titulo = _filtro
	
	elif search != '':
		negocios = negocios.filter(name__contains=search) #| negocios.filter(name__contains=search)
		titulo = search
	
	return render(request, 'lugares/index.html', {'negocios':negocios, 'industries':industries, 'titulo':titulo})

def eventos(request):
	eventos = Evento.objects.all()
	return render(request, 'eventos/index.html', {'eventos': eventos})

def info(request, pk):
	negocio = get_object_or_404(Negocio, pk=pk)
	negocio
	return render(request, 'info/index.html', {'negocio': negocio})
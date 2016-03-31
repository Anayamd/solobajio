from django.shortcuts import render, get_object_or_404
from .models import Negocio, Evento, Industry
from django.db.models import Q

def home(request):
	return render(request, 'home/index.html')

def lugares(request):
	negocios = Negocio.objects.all().exclude(published_date__isnull=True).order_by('ranking')
	industries = Industry.objects.all()
	busqueda = False

	if request.method == 'POST':
		s = request.POST['busqueda']
		negocios = negocios.filter(Q(name__contains=s) | Q(tags__name__contains=s)).distinct()
		busqueda = s
	
	return render(request, 'lugares/index.html', {'negocios':negocios, 'industries':industries, 'busqueda':busqueda})

def lugares_search(request, filtro):
	negocios = Negocio.objects.all().exclude(published_date__isnull=True).filter(Q(industry__ind_type__iexact=filtro) | Q(tags__name__iexact=filtro)).distinct().order_by('ranking')
	industries = Industry.objects.all()
	return render(request, 'lugares/index.html', {'negocios':negocios, 'industries':industries, 'filtro':filtro})

def eventos(request):
	eventos = Evento.objects.all()
	return render(request, 'eventos/index.html', {'eventos': eventos})

def info(request, pk):
	negocio = get_object_or_404(Negocio, pk=pk)
	negocio
	return render(request, 'info/index.html', {'negocio': negocio})
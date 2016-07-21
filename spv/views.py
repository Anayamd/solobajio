from django.shortcuts import render, get_object_or_404, redirect
from .models import Negocio, Evento, Industry
from django.db.models import Q
from .forms import MensajeForm
from django.utils import timezone
from itertools import chain
 
def home(request):
        return render(request, 'home/index.html')

def lugares(request, filtro=None):
        if not filtro:
                negocios = Negocio.objects.all().exclude(published_date__isnull=True).order_by('ranking')
        else:
                negocios = Negocio.objects.all().exclude(published_date__isnull=True).filter(Q(industry__ind_type__iexact=filtro) | Q(tags__name__iexact=filtro)).distinct().order_by('ranking')
        industries = Industry.objects.all()

        if request.method == 'POST':
                s = request.POST['busqueda']
                negocios = negocios.filter(Q(name__contains=s) | Q(tags__name__contains=s)).distinct()
                filtro = s
        
        return render(request, 'lugares/index.html', {'negocios':negocios, 'industries':industries, 'filtro':filtro})

def eventos(request):
        eventos = Evento.objects.all()
        return render(request, 'eventos/index.html', {'eventos': eventos})

def info(request, pk):
        negocio = get_object_or_404(Negocio, pk=pk)
        days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        recomendados = Negocio.objects.exclude(pk=negocio.pk).filter(industry=negocio.industry)[:4]
        if len(recomendados) < 4:
            recomendados = list(chain(recomendados, Negocio.objects.exclude( Q(pk=negocio.pk) | Q(industry=negocio.industry))[:4-len(recomendados)]))
        return render(request, 'info/index.html', {'negocio':negocio, 'days':days, 'recomendados':recomendados})

def mensaje(request):
        if request.method == 'POST':
                print('Entramos a post')
                form = MensajeForm(request.POST)
                print(form)
                if form.is_valid():
                        print('Valid FORM')
                        mensaje = form.save(commit=False)
                        mensaje.fecha = timezone.now()
                        mensaje.save()
        return redirect(request.META.get('HTTP_REFERER'))

def contacto(request):
        return render(request, 'contacto/index.html')

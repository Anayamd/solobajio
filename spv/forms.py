from django import forms
from datetime import datetime

from .models import Mensaje

class MensajeForm(forms.ModelForm):
	class Meta:
		model = Mensaje
		fields = ('email', 'texto')
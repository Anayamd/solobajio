from django import template
import datetime

register = template.Library()

@register.filter(name='array_index')
def array_index(array, index):
	return array[index]

@register.filter(name='array_index_one')
def array_index_one(array, index):
	return array[index-1]
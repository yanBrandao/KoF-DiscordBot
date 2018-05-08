from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
	template = loader.get_template('database/index.html')
	context = {}
	return HttpResponse(template.render(context, request))
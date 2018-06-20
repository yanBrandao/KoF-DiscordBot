from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from database.models import Player
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
	template = loader.get_template('database/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def signUp(request):
	try:
		pEmail = request.POST['email']
		pNick = request.POST['nickname']
		pPassw = request.POST['password']
		pRepassw = request.POST['repeat-password']
		logger.error('-' + pRepassw + '-')
		logger.error('-' + pPassw + '-')
		pCountry = request.POST['country']
		if pPassw == pRepassw:
			logger.error('senha confere')
			p = Player(email = pEmail, nickname = pNick, password = pPassw, victories = 0, defeats = 0, country = pCountry)
			p.save()
		else:
			logger.error('senha errada')
	except:
		logger.error('Theres is no nickname')
	template = loader.get_template('database/signUp.html')
	context = {}
	return HttpResponse(template.render(context, request))
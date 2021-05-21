#first file
from django.http import HttpResponse
from django.shortcuts import render
def index(requests):
	return render(requests ,"index.html")
def about(requests):
	return HttpResponse('we are learning django')
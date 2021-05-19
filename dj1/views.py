#first file
from django.http import HttpResponse
def index(requests):
	return HttpResponse('''<h1 these are some important links </h1> <a href = "https://www.remove.bg/"> click to remove background</a>>''')
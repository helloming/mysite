from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime
from mysite.books.models import Book
from mysite.forms import ContactForm

def hello(request):
	return HttpResponse("hello!!! word")

def current_datetime(request):
	now=datetime.datetime.now()
	return render_to_response("current_datetime.html",{"current_date":now})

def hours_ahead(request,offset):
	try:
		offset=int(offset)
	except ValueError:
		raise Http404()
	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
	html="<html><body>in%s hours later It it now %s</body></html>"%(offset,dt)
	return HttpResponse(html)

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		books=Book.objects.filter(title__icontains=q)
		return render_to_response('search_results.html',{'books':books,'query':q})
	else:
		return render_to_response('please submit a word!')



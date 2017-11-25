from django.shortcuts import render, Http404
from .forms import ContactForm

def home(request):
	template = 'aqp/home.html'
	
	return render(request, template)


def about(request):

	template = 'aqp/about.html'
	context = {
				}
	return render(request, template, context)


def contact(request):
	form_class = ContactForm
	return render(request,'aqp/contact.html', {
	    'form':form_class ,
	})

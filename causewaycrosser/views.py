from django.shortcuts import render
from django.http import HttpResponse
from .services import get_all_images, get_some_images

def index(request):

	all_images = get_all_images() 
	
	some_images = get_some_images(all_images) 

	context_dict = {'message' : "Welcome!", 'some_images' : some_images}
	
	return render(request, 'causewaycrosser/index.html', context_dict)

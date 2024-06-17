from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import logging


logger = logging.getLogger(__name__)

def index(request):
    logger.info('index page accessed')
    Response = render_to_string("myapp/main.html")
    return HttpResponse(Response)

def about(request):
    logger.info('about page accessed')
    Response = render_to_string("myapp/about.html")
    return HttpResponse(Response)

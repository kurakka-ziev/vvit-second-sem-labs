from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'static_handler.html')
def hello(request):
    return HttpResponse('Hello, World!')#, content_type="text/plain")

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''congragulations, you have created a web application''')

# Create your views here.

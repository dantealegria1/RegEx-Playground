from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Home Page!")

def reverse_string_ui(request):
    return render(request, 'reverse_string.html')

def regex_generator_ui(request):
    return render(request,'regex_generator.html')

def regex_testing_ui(request):
    return render(request, 'regex_testing.html')

def regex_normal_ui(request):
    return render(request, 'regex_normal.html')


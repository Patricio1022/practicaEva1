from django.shortcuts import render

from django.http import HttpResponse

def vista1(request):
    return HttpResponse("Hola, esta es la vista 1 de la primera app.")

def vista2(request):
    return HttpResponse("Hola, esta es la vista 2 de la primera app.")

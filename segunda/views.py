from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido a la vista inicio de la segunda app.")

def contacto(request):
    return HttpResponse("Esta es la vista de contacto de la segunda app.")

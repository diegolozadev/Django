from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def days_week(request, day):
    quote_tex = None
    if day == "monday":
        quote_tex = "Pienso, luego existo"
    elif day == "tuesday":
        quote_tex = "La vida es bella"
    elif day == "wednesday":
        quote_tex = "Belleza de día"
    else:
        return HttpResponseNotFound("No hay frase para este día")
    
    return HttpResponse(quote_tex)
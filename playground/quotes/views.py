from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

days_of_week = {
    "monday": "Pienso, luego existo",
    "tuesday": "La vida es bella",
    "wednesday": "Belleza de día",
    "thursday": "Carpe diem",
    "friday": "Vive y deja vivir",
    "saturday": "El tiempo es oro",
    "sunday": "Aprovecha el día",
}

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El día no existe")
    redirect_day = days[day-1]
    return HttpResponseRedirect(f"/quotes/{redirect_day}")
    
    
def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("No hay frase para este día")
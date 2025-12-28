from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
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

def index(request):
    days = list(days_of_week.keys())
    return render(request, "quotes/quotes.html", {
        "days": days,
    })


def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El día no existe")
    redirect_day = days[day-1]
    redirect_path = reverse("day-quote", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)
    

def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except Exception:
        # return HttpResponseNotFound("No hay frase para este día")
        raise Http404()
    

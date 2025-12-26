from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

def home(request):
    today = date.today()
    stack = [
            {'id': 'python', 'name': 'Python'},
            {'id': 'django', 'name': 'Django'},
            {'id': 'react', 'name': 'React'},
            {'id': 'php', 'name': 'PHP'},
            ]

    return render(request, "landing/landing.html", {
        "name": "fernando",
        "age": 28,
        "today": today,
        "stack": stack,
    })

def stack_detail(request, tool):
    return HttpResponse(f"Tecnología: {tool}")
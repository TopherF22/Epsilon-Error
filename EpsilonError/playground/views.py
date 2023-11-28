from django.shortcuts import render
from django.http import HttpResponse



def playground(request):
    return render(request, 'playground.html', {})
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(render(request, 'index.html'))

def resume(request):
    return HttpResponse(render(request, 'resume.html'))

def projects(request):
    return HttpResponse(render(request, 'projects.html'))

def saralu(request):
    return HttpResponse('momkey')
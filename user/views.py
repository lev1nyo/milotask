from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import UserNew


def list(request):
    template = loader.get_template('list.html')
    context = {
        'users': UserNew.objects.all()
    }
    return HttpResponse(template.render(context, request))


def view(request):
    pass

def edit(request):
    pass

def delete(request):
    pass
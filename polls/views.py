from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = "<h1>Заголовок</h1>" \
              "<h2>Подзаголовок</h2>"
    return HttpResponse(context)

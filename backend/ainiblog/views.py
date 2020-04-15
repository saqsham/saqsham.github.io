from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    t = TemplateResponse(request, 'index.html', {})
    return t.render()


def about(request):
    t = TemplateResponse(request, 'about.html', {})
    return t.render()


def chatroom(request):
    t = TemplateResponse(request, 'chat/room.html', {})
    return t.render()


def firstpost(request):
    t = TemplateResponse(request, 'posts/2020/1/post.html', {})
    return t.render()
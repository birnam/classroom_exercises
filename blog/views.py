from django.http import HttpResponse
from blog.models import *
from django.shortcuts import render

def list(request):
    return render(request, "listing.html", {'entries': Entry.objects.all()}, content_type="text/html")

def list_old(request):
    titles = []
    for e in Entry.objects.all():
        titles += [formatListElement(e)]

    return HttpResponse("<ul>{0}</ul>".format("".join(titles)))

def detail(request, entry_id):
    return render(request, "detail.html", {'entry': Entry.objects.get(id=entry_id)})

def detail_old(request, entry_id):
    e = Entry.objects.get(id=entry_id)
    return HttpResponse("<h1>{0}</h1><p><em>{1}</em></p><p>{2}</p>".format(e.title, e.pub_date, e.body))

def formatListElement(e):
    return "<li><a href=\"{0}\">{1}</a></li>".format("/blog/entry/{0}".format(e.id), e.title)
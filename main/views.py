import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import logout


from .models import *

def index(request):
  
    banner = Page.objects.filter(slug="welcome-banner").first()
    chapbooks = Chapbook.objects.filter(publish=True)
    return render(request, "index.html", 
            {
            'banner':banner,
            'chapbooks':chapbooks,
            } )

def view(request, id):
    ''
    chapbook = Chapbook.objects.filter(id=id).first()
    return render(request, "chapbook.html", {'chapbook': chapbook,} )

def search(request):
    query = request.GET.get("q", False)
    results = []

    if query:
        chapbooks = Chapbook.objects.filter( Q(name__contains=query)|Q(text__contains=query)|Q(preamble__contains=query))
       
    results = list(chapbooks)

    return render(request, "searchresults.html", {'results': results,} )


def page(request, slug):
    ''
    page = Page.objects.filter(slug=slug).first()
    return render(request, "page.html", {'page': page,} )

def do_logout(request):
    logout(request)

    return redirect("/")

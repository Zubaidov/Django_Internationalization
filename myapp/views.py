from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


def index(request):
    context = {}
    return render(request, 'index.html', context)

def aboutus(request):
    context={}
    return render(request, 'aboutus.html', context)

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text
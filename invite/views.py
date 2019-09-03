# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Invite


def index(request):
    return HttpResponse('Ikke noe her enda.')


def card(request, slug):
    '''
        The birthday card
    '''
    slug = slug.replace("-", " ")
    if "og" in slug:
        names = [name.capitalize() for name in slug.split(" og ")]
        name = " og ".join(names)
    else:
        if " " in slug:
            name = " ".join([name.capitalize() for name in slug.split(" ")])
        else:
            name = slug.capitalize()
    invite = get_object_or_404(Invite, name=name)
    return render(request, 'card.svg', {'name': invite.name, 'object': invite}, content_type='image/svg+xml')


def cards(request):
    invites = get_list_or_404(Invite)
    return render(request, 'cards.html', {'cards': invites})

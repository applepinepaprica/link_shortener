# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import redirect

from .models import Link


def index(request, url):
    try:
        link = Link.objects.get(short_link=url)
    except Link.DoesNotExist:
        raise Http404("Question does not exist")
    return redirect(link.full_link)

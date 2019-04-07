# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myproject.link_shortener.models import Link, LinkInfo

admin.site.register(Link)
admin.site.register(LinkInfo)

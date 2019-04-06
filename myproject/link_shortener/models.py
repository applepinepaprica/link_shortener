# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Link(models.Model):
    short_link = models.CharField(max_length=10)
    full_link = models.CharField(max_length=100)

    def __str__(self):
        return self.full_link

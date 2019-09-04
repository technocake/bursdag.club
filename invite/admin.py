# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.template.defaultfilters import slugify

from .models import Invite



admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)


class InviteAdmin(admin.ModelAdmin):
    list_display = ('name', 'pokemon', 'status')
    dynamic_field_order = ('name', 'pokemon', 'status')
    search_fields = ('name', 'pokemon', 'status')
    sortable = ('name', 'pokemon', 'status')


    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('invite/', self.invite),
        ]
        return my_urls + urls

    def view_on_site(self, obj):
        url = reverse('card', kwargs={'slug': slugify(obj.name)})
        return url

    def invite(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           name = 'Yoanna',
        )
        return TemplateResponse(request, "card.svg", context)


admin.site.register(Invite, InviteAdmin)

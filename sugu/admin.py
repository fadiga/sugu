#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: FADIGA

from django.contrib import admin

from models import (Owner, Organization, Order, OrderItem,
                    TypeOrganization)


class OItemInline(admin.TabularInline):
    # model = OrderItem
    pass


class OrdInline(admin.TabularInline):
    # model = Order
    pass


class OrgInline(admin.TabularInline):
    # model = Organization
    pass


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class TypeOrganizationAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'address',
                    'address_extra', 'legal_infos', 'create_date')
    list_display_links = ('__str__', 'name', 'address',
                          'address_extra', 'legal_infos', 'create_date')
    list_filter = ('create_date', 'owner', 'name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date',
                    'number', 'subject', 'organization',)
    list_filter = ('date', 'organization__name',)
    # inlines = [OItemInline, ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order', 'description',
                    'quantity', 'price',)
    list_filter = ('order__number',)

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(TypeOrganization, TypeOrganizationAdmin)

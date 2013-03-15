#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: FADIGA

from django.contrib import admin

from models import (Owner, Organization, Supplier, Order, OrderItem,
                    TypeOrganization)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


class TypeOrganizationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    list_filter = ('full_name',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'address',
                    'address_extra', 'legal_infos', 'create_date')
    list_filter = ('create_date', 'owner', 'name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'supplier',
                    'number', 'subject',)
    list_filter = ('date', 'organization', 'supplier',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'order', 'description', 'quantity', 'price',)
    list_filter = ('order__number',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(TypeOrganization, TypeOrganizationAdmin)

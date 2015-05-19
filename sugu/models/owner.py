#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy, ugettext as _


class Owner(User):
    """ The web user who is also owner of the Organization
    """

    class Meta:
        app_label = 'sugu'
        verbose_name = _("Owner")
        verbose_name_plural = _("Owners")

    phone = models.CharField(max_length=30, blank=True,
                             verbose_name=("Telephone"))
    address_email = models.EmailField(blank=True,
                                      verbose_name=("Adresse électronique"))

    def __str__(self):
        return _("%(name)s") % {"name": self.username}


class CategoryOrg(models.Model):

    class Meta:
        app_label = 'sugu'
        verbose_name = _("CategoryOrganization")
        verbose_name_plural = _("CategoryOrganizations")

    name = models.CharField(max_length=150,
                            verbose_name=("Type d'organisation"),
                            help_text=ugettext_lazy("Type d'organisation"))

    def __str__(self):
        return _("%(name)s") % {"name": self.name}


class TypeOrganization(models.Model):
    """ Represents the type organization
    """

    class Meta:
        app_label = 'sugu'
        verbose_name = _("TypeOrganization")
        verbose_name_plural = _("TypeOrganizations")

    name = models.CharField(max_length=150,
                            verbose_name=("Type d'organisation"),
                            help_text=ugettext_lazy("Type d'organisation"))

    def __str__(self):
        return _("%(name)s") % {"name": self.name}


class Organization(models.Model):
    """ Represents the company emmiting the orders
    """

    class Meta:
        app_label = 'sugu'
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    create_date = models.DateTimeField(verbose_name=("Date d'enregistrement"),
                                       default=datetime.today())
    name = models.CharField(max_length=150,
                            verbose_name=("Nom de votre entreprise"))
    type_org = models.ForeignKey(TypeOrganization, related_name='types',
                                 verbose_name=("Type d'organisation"))
    address = models.TextField(blank=True,
                               verbose_name=("Adresse principale\
                                                           de votre société"))
    address_extra = models.CharField(blank=True, max_length=20,
                                     verbose_name=("Numero de téléphone\
                                                        de votre entreprise"))
    address_email = models.EmailField(blank=True,
                                      verbose_name=("Adresse électronique\
                                                        de votre entreprise"))
    legal_infos = models.TextField(blank=True,
                                   verbose_name=("Informations légales"))
    owner = models.ForeignKey(Owner, related_name='owners',
                              verbose_name=("Proprietaire"))
    image = models.ImageField(upload_to='org_images/', blank=True,
                              verbose_name=("image de la societe"))

    def __str__(self):
        return _("%(name)s") % {"name": self.name}

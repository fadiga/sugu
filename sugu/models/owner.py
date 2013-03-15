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

    phone = models.CharField(max_length=30, blank=True,
                                                   verbose_name=("Telephone"))
    address_email = models.EmailField(blank=True,
                                      verbose_name=("Adresse électronique"))

    def __unicode__(self):
        return _(u'%(name)s') % {"name": self.username}


class TypeOrganization(models.Model):
    """ Represents the type organization
    """

    class Meta:
        app_label = 'sugu'
    name = models.CharField(max_length=150,
                            verbose_name=("Type d'organisation"),\
                               help_text=ugettext_lazy("Type d'organisation"))

    def __unicode__(self):
        return _(u'%(name)s') % {"name": self.name}


class Organization(models.Model):
    """ Represents the company emmiting the orders
    """

    class Meta:
        app_label = 'sugu'

    create_date = models.DateTimeField(verbose_name=("Date d'enregistrement"),
                                                     default=datetime.today())
    name = models.CharField(max_length=150,
                                     verbose_name=("Nom de votre entreprise"))
    type_org = models.ForeignKey(TypeOrganization, related_name='types',
                                         verbose_name=("Type d'organisation"))
    address = models.TextField(blank=True,
                                          verbose_name=("Adresse principale\
                                                           de votre société"))
    address_extra = models.CharField(blank=True, max_length=20,\
                                    verbose_name=("Numero de téléphone\
                                                        de votre entreprise"))
    address_email = models.EmailField(blank=True,
                                      verbose_name=("Adresse électronique\
                                                        de votre entreprise"))
    legal_infos = models.TextField(blank=True,
                                        verbose_name=("Informations légales"))
    owner = models.ForeignKey(Owner, related_name='owner',
                                                verbose_name=("Proprietaire"))
    image = models.ImageField(upload_to='org_images/', blank=True,
                                         verbose_name=("image de la societe"))

    def __unicode__(self):
        return _(u'%(name)s') % {"name": self.name}


class Supplier(models.Model):
    """ Represents the Fournisseur
    """

    class Meta:
        app_label = 'sugu'

    full_name = models.CharField(max_length=150,
                            verbose_name=("Nom du client"),\
                                     help_text=ugettext_lazy("Supplier Name"))
    address_email = models.EmailField(blank=True,
                                      verbose_name=("Adresse électronique\
                                                       de votre Fournisseur"))
    address = models.TextField(blank=True, verbose_name=("Adresse du client"))
    organization = models.ForeignKey(Organization,\
                                             verbose_name=(_("Organization")))

    def __unicode__(self):
        return _(u"%(name)s") % {'name': self.full_name}

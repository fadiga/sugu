#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy, ugettext as _
from owner import Organization


class Order(models.Model):
    """ Represents an order
    """
    class Meta:
        app_label = 'sugu'
        verbose_name = _("Order")

    number = models.IntegerField(verbose_name=("Numero"))
    date = models.DateField(verbose_name=("Fait le"),
                            default=datetime.today)
    subject = models.CharField(max_length=100, blank=True,
                               verbose_name=("Objet"))
    organization = models.ForeignKey(Organization,
                                     verbose_name=("Fournisseur"),
                                     related_name='Orders')

    @classmethod
    def get_next_number(cls, org):
        """
            Get a valid number automatically incremented from
            the higher one.
        """
        orders = Order.objects.filter(organization=org)
        number = 1
        if orders.count():
            last_order = orders.latest('number')
            number += int(last_order.number)
        return number

    def __str__(self):
        return _("%(num)s - %(org)s : %(subject)s") \
                                        % {'num': self.number,
                                           'org': self.organization,
                                           'subject': self.subject}


class OrderItem(models.Model):
    """ Represents an element of an order such as a product
    """
    class Meta:
        app_label = 'sugu'
        verbose_name = _("OrderItem")

    U_CARTON = 'C'
    U_P = 'P'
    U_L = 'L'
    U_K = 'K'
    U_CHOICES = (
        (U_CARTON, "Carton"),
        (U_P, "Pièce"),
        (U_K, "Kg"),
        (U_L, "Littre"))

    order = models.ForeignKey(Order, blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name=("Quantite"))
    unit = models.CharField("unite", max_length=1, choices=U_CHOICES)
    description = models.CharField(max_length=50,
                                   verbose_name=("Description"))
    price = models.PositiveIntegerField(verbose_name=("Prix Unitiare"))

    def __str__(self):
        return _("%(desc)s %(qty)s %(price)s") % {'qty': self.quantity,
                                                   'desc': self.description,
                                                   'price': self.price}

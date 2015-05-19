# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Type d'organisation", max_length=150, verbose_name=b"Type d'organisation")),
            ],
            options={
                'verbose_name': 'CategoryOrganization',
                'verbose_name_plural': 'CategoryOrganizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name=b'Numero')),
                ('date', models.DateField(default=datetime.datetime.today, verbose_name=b'Fait le')),
                ('subject', models.CharField(max_length=100, verbose_name=b'Objet', blank=True)),
            ],
            options={
                'verbose_name': 'Order',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name=b'Quantite')),
                ('unit', models.CharField(max_length=1, verbose_name='unite', choices=[(b'C', 'Carton'), (b'P', 'Pi\xe8ce'), (b'K', 'Kg'), (b'L', 'Littre')])),
                ('description', models.CharField(max_length=50, verbose_name=b'Description')),
                ('price', models.PositiveIntegerField(verbose_name=b'Prix Unitiare')),
                ('order', models.ForeignKey(blank=True, to='sugu.Order', null=True)),
            ],
            options={
                'verbose_name': 'OrderItem',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2015, 4, 3, 14, 5, 35, 23893), verbose_name=b"Date d'enregistrement")),
                ('name', models.CharField(max_length=150, verbose_name=b'Nom de votre entreprise')),
                ('address', models.TextField(verbose_name=b'Adresse principale                                                           de votre soci\xc3\xa9t\xc3\xa9', blank=True)),
                ('address_extra', models.CharField(max_length=20, verbose_name=b'Numero de t\xc3\xa9l\xc3\xa9phone                                                        de votre entreprise', blank=True)),
                ('address_email', models.EmailField(max_length=75, verbose_name=b'Adresse \xc3\xa9lectronique                                                        de votre entreprise', blank=True)),
                ('legal_infos', models.TextField(verbose_name=b'Informations l\xc3\xa9gales', blank=True)),
                ('image', models.ImageField(upload_to=b'org_images/', verbose_name=b'image de la societe', blank=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=30, verbose_name=b'Telephone', blank=True)),
                ('address_email', models.EmailField(max_length=75, verbose_name=b'Adresse \xc3\xa9lectronique', blank=True)),
            ],
            options={
                'verbose_name': 'Owner',
                'verbose_name_plural': 'Owners',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='TypeOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Type d'organisation", max_length=150, verbose_name=b"Type d'organisation")),
            ],
            options={
                'verbose_name': 'TypeOrganization',
                'verbose_name_plural': 'TypeOrganizations',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organization',
            name='owner',
            field=models.ForeignKey(related_name='owners', verbose_name=b'Proprietaire', to='sugu.Owner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='type_org',
            field=models.ForeignKey(related_name='types', verbose_name=b"Type d'organisation", to='sugu.TypeOrganization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='organization',
            field=models.ForeignKey(related_name='Orders', verbose_name=b'Fournisseur', to='sugu.Organization'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-06 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_property', to='shop.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category property',
                'verbose_name_plural': 'Category properties',
            },
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('value', models.CharField(default='', max_length=250, verbose_name='Value')),
                ('category_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_property', to='properties.CategoryProperty', verbose_name='Propery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_product', to='shop.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product property',
            },
        ),
    ]
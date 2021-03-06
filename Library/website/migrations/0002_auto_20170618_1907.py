# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebook',
            old_name='book',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='issuebook',
            old_name='user',
            new_name='libraryUser',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='status',
        ),
        migrations.AddField(
            model_name='book',
            name='bookID',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('1', '1'), ('0', '0')], default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='issuebook',
            name='fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='issuebook',
            name='noOfDays',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='userID',
            field=models.CharField(default=1, max_length=10),
        ),
    ]

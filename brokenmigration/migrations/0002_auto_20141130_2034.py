# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokenmigration', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Thing',
        ),
        migrations.AlterField(
            model_name='thinglist',
            name='things',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]

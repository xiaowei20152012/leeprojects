# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunuser', '0002_auto_20160516_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunuser', '0003_usertoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserToken',
        ),
    ]

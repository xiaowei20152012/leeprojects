# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=50)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('n_comments', models.IntegerField()),
                ('n_pingbacks', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('authors', models.ManyToManyField(to='sunuser.Author')),
                ('blog', models.ForeignKey(to='sunuser.Blog')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='job',
        ),
        migrations.AlterField(
            model_name='user',
            name='QQ',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name=b'QQ', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=50, null=True, verbose_name=b'\xe7\x9b\xae\xe5\x89\x8d\xe6\x89\x80\xe5\x9c\xa8\xe5\x9f\x8e\xe5\xb8\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='province',
            field=models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=50, null=True, verbose_name=b'\xe7\x9b\xae\xe5\x89\x8d\xe6\x89\x80\xe5\x9c\xa8\xe7\x9c\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95token', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weChat',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1', blank=True),
        ),
    ]

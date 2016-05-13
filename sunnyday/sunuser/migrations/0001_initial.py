# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=20, null=True, verbose_name=b'\xe8\x81\x8c\xe4\xb8\x9a', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=20, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='RolesPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roles_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdPartyRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('third_party_id', models.CharField(max_length=50, verbose_name=b'\xe4\xb8\x89\xe6\x96\xb9\xe7\x99\xbb\xe5\xbd\x95\xe8\xaf\x86\xe5\x88\xabid')),
                ('third_party_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'', max_length=60, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True)),
                ('nickname', models.CharField(default=b'', max_length=40, null=True, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0', blank=True)),
                ('password', models.CharField(default=b'', max_length=100, null=True, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81', blank=True)),
                ('email', models.CharField(default=b'', max_length=60, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('avatar', models.URLField(default=b'', null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
                ('mobile', models.CharField(default=b'', max_length=20, null=True, verbose_name=b'\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('birthday', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(default=b'\xe7\x94\xb7', max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('QQ', models.CharField(default=b'', max_length=60, null=True, verbose_name=b'QQ', blank=True)),
                ('weChat', models.CharField(default=b'', max_length=80, null=True, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1', blank=True)),
                ('microBlog', models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a', blank=True)),
                ('douban', models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xe8\xb1\x86\xe7\x93\xa3', blank=True)),
                ('country', models.CharField(default=b'\xe4\xb8\xad\xe5\x9b\xbd', max_length=50, null=True, verbose_name=b'\xe7\x9b\xae\xe5\x89\x8d\xe6\x89\x80\xe5\x9c\xa8\xe5\x9b\xbd\xe5\xae\xb6', blank=True)),
                ('province', models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=50, null=True, verbose_name=b'\xe7\x9b\xae\xe5\x89\x8d\xe6\x89\x80\xe5\x9c\xa8\xe7\x9a\x84\xe7\x9c\x81\xe4\xbb\xbd', blank=True)),
                ('city', models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=50, null=True, verbose_name=b'\xe7\x9b\xae\xe5\x89\x8d\xe6\x89\x80\xe5\x9c\xa8\xe7\x9a\x84\xe5\x9f\x8e\xe5\xb8\x82', blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('enable', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('pw_salt', models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81\xe7\x9b\x90')),
                ('token', models.CharField(default=b'', max_length=128, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95token')),
                ('token_utime', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95token\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('uid', models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xe5\x94\xaf\xe4\xb8\x80\xe8\xaf\x86\xe5\x88\xabid', blank=True)),
                ('sign', models.CharField(default=b'', max_length=200, null=True, verbose_name=b'\xe4\xb8\xaa\xe6\x80\xa7\xe7\xad\xbe\xe5\x90\x8d', blank=True)),
                ('job', models.ForeignKey(blank=True, to='sunuser.Job', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('roles_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='thirdpartyrelation',
            name='user',
            field=models.ForeignKey(to='sunuser.User'),
        ),
    ]

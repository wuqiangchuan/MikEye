# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-06 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('condition', models.TextField(verbose_name='\u544a\u8b66\u6761\u4ef6')),
                ('interval', models.IntegerField(default=300, verbose_name='\u544a\u8b66\u95f4\u9694')),
                ('recover_notice', models.BooleanField(default=True, verbose_name='\u6545\u969c\u6062\u590d\u540e\u662f\u5426\u53d1\u9001\u901a\u77e5')),
                ('recover_subject', models.CharField(blank=True, max_length=128, null=True)),
                ('recover_message', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActionOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('step', models.SmallIntegerField(default=1, verbose_name='\u7b2cn\u6b21\u544a\u8b66')),
                ('action_type', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS'), ('script', 'RunScript')], default='email', max_length=128, verbose_name='\u52a8\u4f5c\u7c7b\u578b')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u7ec4\u540d\u5b57')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u4e3b\u673a\u540d\u79f0')),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('monitor_by', models.CharField(choices=[('agent', 'agent'), ('snmp', 'snmp'), ('wget', 'wget')], max_length=64, verbose_name='\u76d1\u63a7\u65b9\u5f0f')),
                ('status', models.IntegerField(choices=[(1, 'Online'), (2, 'Down'), (3, 'Uncreachble'), (4, 'Offline')], default=1, verbose_name='\u72b6\u6001\u4fe1\u606f')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
                ('host_groups', models.ManyToManyField(blank=True, to='monitor01.HostGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('content', models.TextField(verbose_name='\u7ef4\u62a4\u7684\u5185\u5bb9')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('host_groups', models.ManyToManyField(blank=True, to='monitor01.HostGroup')),
                ('hosts', models.ManyToManyField(blank=True, to='monitor01.Hosts')),
            ],
        ),
        migrations.CreateModel(
            name='NotifiersUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='\u90ae\u7bb1')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u63d2\u4ef6\u540d\u79f0(\u6a21\u5757\u540d)')),
                ('interval', models.IntegerField(default=60, verbose_name='\u76d1\u63a7\u95f4\u9694')),
                ('plugin_name', models.CharField(default='n/a', max_length=60, verbose_name='\u670d\u52a1\u540d(\u51fd\u6570\u540d)')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u6307\u6807\u540d\u79f0')),
                ('item_key', models.CharField(max_length=64, verbose_name='\u670d\u52a1\u6307\u6807\u7684key')),
                ('data_type', models.CharField(choices=[('int', 'int'), ('float', 'float'), ('str', 'string')], default='int', max_length=32, verbose_name='\u6570\u636e\u7c7b\u578b')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u6a21\u677f\u540d\u79f0')),
                ('service', models.ManyToManyField(to='monitor01.Service', verbose_name='\u670d\u52a1\u5217\u8868')),
            ],
        ),
        migrations.CreateModel(
            name='Triggers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u89e6\u53d1\u5668\u540d')),
                ('expression', models.TextField(verbose_name='\u8868\u8fbe\u5f0f')),
                ('sericety', models.IntegerField(choices=[(1, 'Information'), (2, 'Warning'), (3, 'Average'), (4, 'Hight'), (5, 'Diaster')], verbose_name='\u544a\u8b66\u7ea7\u522b')),
                ('enabled', models.BooleanField(default=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='WebAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=40)),
                ('EmailPopAddress', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='templates',
            name='triggers',
            field=models.ManyToManyField(blank=True, to='monitor01.Triggers', verbose_name='\u89e6\u53d1\u5668\u5217\u8868'),
        ),
        migrations.AddField(
            model_name='service',
            name='items',
            field=models.ManyToManyField(blank=True, to='monitor01.ServiceIndex', verbose_name='\u6307\u6807\u5217\u8868'),
        ),
        migrations.AddField(
            model_name='hosts',
            name='templates',
            field=models.ManyToManyField(blank=True, to='monitor01.Templates'),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='templates',
            field=models.ManyToManyField(blank=True, to='monitor01.Templates'),
        ),
        migrations.AddField(
            model_name='actionoperation',
            name='notifiers',
            field=models.ManyToManyField(blank=True, to='monitor01.NotifiersUser', verbose_name='\u901a\u77e5\u5bf9\u8c61'),
        ),
        migrations.AddField(
            model_name='action',
            name='host',
            field=models.ManyToManyField(blank=True, to='monitor01.Hosts'),
        ),
        migrations.AddField(
            model_name='action',
            name='host_group',
            field=models.ManyToManyField(blank=True, to='monitor01.HostGroup'),
        ),
        migrations.AddField(
            model_name='action',
            name='operations',
            field=models.ManyToManyField(to='monitor01.ActionOperation'),
        ),
    ]

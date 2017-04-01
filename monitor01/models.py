#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from click.types import Choice
from django.template.defaultfilters import default
#from bsddb.test.test_all import verbose

# Create your models here.

class WebAdmin(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=50)
    Email = models.CharField(max_length=40)
    EmailPopAddress = models.CharField(max_length=60)
    def __unicode__(self):
        return self.Email


class ServiceIndex(models.Model):
    name = models.CharField(u'指标名称',max_length=64)
    item_key = models.CharField(u'服务指标的key',max_length=64)
    data_type_choice=(
            ('int','int'),
            ('float','float'),
            ('str','string')
            )
    data_type = models.CharField(u'数据类型',max_length=32,choices=data_type_choice,default='int')
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return "%s,%s" %(self.name,self.item_key)
    
class Service(models.Model):    
    name = models.CharField(u'插件名称(模块名)',max_length=64,unique=True)
    interval = models.IntegerField(u'监控间隔',default=60)
    plugin_name = models.CharField(u'服务名(函数名)',max_length=60,default='n/a')
    items = models.ManyToManyField('ServiceIndex',verbose_name=u'指标列表',blank=True)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return self.name

class Templates(models.Model):  
    name = models.CharField(u'模板名称',max_length=32,unique=True)
    service = models.ManyToManyField('Service',verbose_name=u'服务列表')
    triggers = models.ManyToManyField('Triggers',verbose_name=u'触发器列表',blank=True)
    def __unicode__(self):
        return self.name
    
class Triggers(models.Model):
    name = models.CharField(u'触发器名',max_length=32)
    expression = models.TextField(u'表达式')
    servicety_choices=(
            (1,'Information'),
            (2,'Warning'),
            (3,'Average'),
            (4,'Hight'),
            (5,'Diaster'),
            )
    sericety = models.IntegerField(u'告警级别',choices=servicety_choices)
    enabled = models.BooleanField(default=True)
    memo=models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return self.name

class Hosts(models.Model):    
    name = models.CharField(u'主机名称',max_length=64,unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    #PubIpAddr = models.GenericIPAddressField(unique=True)
    host_groups= models.ManyToManyField('HostGroup',blank=True)
    templates = models.ManyToManyField('Templates',blank=True)
    monitor_by_choices=(
        ('agent','agent'),
        ('snmp','snmp'),
        ('wget','wget'),
        )
    monitor_by=models.CharField(u'监控方式',max_length=64,choices=monitor_by_choices)
    status_choices=(
        (1,'Online'),
        (2,'Down'),
        (3,'Uncreachble'),#不能到达的
        (4,'Offline'),            
        )
    status = models.IntegerField(u'状态信息',choices=status_choices,default=1)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return self.name
    
class HostGroup(models.Model):
    name = models.CharField(u'组名字',max_length=32,unique=True)
    templates = models.ManyToManyField("Templates",blank=True)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return self.name
#Action为触发的动作
class Action(models.Model):
    name = models.CharField(max_length=64,unique=True)
    host_group = models.ManyToManyField("HostGroup",blank=True)
    host = models.ManyToManyField("Hosts",blank=True)
    
    condition= models.TextField(u'告警条件')
    interval = models.IntegerField(u'告警间隔',default=300)
    operations = models.ManyToManyField('ActionOperation')
    
    recover_notice = models.BooleanField(u'故障恢复后是否发送通知',default=True)
    recover_subject = models.CharField(max_length=128,blank=True,null=True)
    recover_message = models.TextField(blank=True,null=True)
    
    enabled = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
#Operation动作中心   
class ActionOperation(models.Model):
    name = models.CharField(max_length=32)
    step = models.SmallIntegerField(u'第n次告警',default=1)
    action_type_choice=(
        ('email','Email'),
        ('sms','SMS'),
        ('script','RunScript'),
            )
    action_type = models.CharField(u'动作类型',choices=action_type_choice,default='email',max_length=128)
    notifiers = models.ManyToManyField('NotifiersUser',verbose_name=u'通知对象',blank=True)
    def __unicode__(self):
        return self.name

class NotifiersUser(models.Model):
    name = models.CharField(max_length=32,unique=True,blank=True)
    email = models.EmailField(u'邮箱',unique=True)
    def __unicode__(self):
        return self.name
    
class Maintenance(models.Model):
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField('Hosts',blank=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True)
    
    content = models.TextField(u'维护的内容')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __unicode__(self):
        return self.name
    
    

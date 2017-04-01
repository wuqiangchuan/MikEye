#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
import models
from django.http.response import HttpResponse
import json
class ClientHander(object):
    def __init__(self,client_id):
        self.client_id = client_id
        self.ClientConfigs = { 'service': {},}
        
    def fetch_configs(self):       #用于获取客户端对应的id
        try:
            ClientObj = models.Hosts.objects.get(id=self.client_id)
            #下面把这个client_id关联的template取出来
            TemplateList =  list(ClientObj.templates.select_related())
        
            #由于定义的时候也关联到HostGroup这，所以也要取出HostGroup中对应的
            #即先定位到Host中的host_group字段关联的HostGroup
            for HostGroupObj in ClientObj.host_groups.select_related():
                #再从HostGroup字段定位到Template
                TemplateList.extend(HostGroupObj.templates.select_related())
                TemplateList=list(set(TemplateList))
            for Item in TemplateList:
                print '服务的监控项有: ',Item.service.select_related() 
                for service in Item.service.select_related():   
                    self.ClientConfigs['service'][service.name] = [service.plugin_name,service.interval]    
                    print self.ClientConfigs
            #这样获取也可以，注意这里是多表的关系。
            ''' for I in ClientObj.templates.all():
                print "tempalte_name",I.name 
               
                b = I.service.all()
                for X in b:
                    print X.name ''' 
                      
            return self.ClientConfigs
        except Exception,e:
            print e,"获取关联表时发生错误"
            return 'error'
        #return 'test.......'
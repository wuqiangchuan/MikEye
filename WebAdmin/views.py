#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####

from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import Http404
import json
from monitor01 import models as Monitor
from HardWareInfo import models as HWI


# Create your views here.
def Index(request): 
    #Monitor.WebAdmin.objects.get()
    if request.method == 'GET':
        obj = HWI.HostName.objects.get(HostName='127.0.0.1')
        localinfo = obj.hardinfo_set.all()
        DiskInfo = obj.diskinfo_set.all()
         
        return render_to_response('html/index.html',{'Data':localinfo,'DiskInfo':DiskInfo})
   
    #return HttpResponse(json.dumps('hello django.'))
 
    
def Login(request):
    if request.method == 'GET':
        #raise Http404()  #触发404错误页面
        return render_to_response('Login.html')
    #return HttpResponse(json.dumps('hello django.'))
    if request.method == 'POST':
        name   = request.POST.get('username',None)
        passwd = request.POST.get('passwd',None)
        print name,passwd
        if all([name,passwd]):
            #return HttpResponseRedirect('/index')
            return redirect('/index')


def ChangePWD(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        pwd = request.POST.get('pwd',None)
        Update_Email = request.POST.get('Update_Email',None)
        EmailPopAddress = request.POST.get('EmailPop3Address',None)
        
        if  Monitor.WebAdmin.objects.filter(Username=username):
            Monitor.WebAdmin.objects.all().update(Username=username,Password=pwd,Email=Update_Email,EmailPopAddress=EmailPopAddress)
       
        else:
            Monitor.WebAdmin.objects.create(Username=username,Password=pwd,Email=Update_Email,EmailPopAddress=EmailPopAddress)
       
        #return render_to_response('index.html')      
    return render_to_response('html/index.html')      
          
          
#资产
def CheckAsset(request):
   
    if request.method == 'GET':
        HwiObj = HWI.HostName.objects.all()
        
        #HardInfoObj = HwiObj.hardinfo_set.all()
        '''HwiInfo = HWI.HardInfo.objects.all()
        for I in HwiObj:
            print I,'---',I.hardinfo_set.all()
            data[I] = I.hardinfo_set.all()
            print type(data[I]),data[I]
        print "========="
        print data '''
        DiskObj = HWI.DiskInfo.objects.all()
        
        
        return render_to_response('html/CheckAsset.html',{'HwiObj':HwiObj,'DiskObj':DiskObj})
          
          
          
          
def AddAsset(request):
    if request.method == 'GET':
        HwiObj = HWI.HostName.objects.all()
        
        #HardInfoObj = HwiObj.hardinfo_set.all()
        '''HwiInfo = HWI.HardInfo.objects.all()
        for I in HwiObj:
            print I,'---',I.hardinfo_set.all()
            data[I] = I.hardinfo_set.all()
            print type(data[I]),data[I]
        print "========="
        print data '''
        DiskObj = HWI.DiskInfo.objects.all() 
    
    return render_to_response('html/AddAsset.html', {'HwiObj':HwiObj,'DiskObj':DiskObj})
          
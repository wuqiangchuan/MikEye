#coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http.response import HttpResponse
# Create your views here.
from serilalizer import ClientHander
import json 
from HardWareInfo import models as HWI
from comm import ReturnClientIP

def ClientConfig(request,client_id):  #后一个参数client_id
    print "----client ip----",client_id
    ConfigObj = ClientHander(client_id)
    config = ConfigObj.fetch_configs()
    #print "some thins",config
    
    if config:
        
        #print "return instan",config
        return HttpResponse(json.dumps(config))
        
def ClientError(request):
    ErrorMsg='Access not found.  404 page'
    return HttpResponse(json.dumps(ErrorMsg))






#-------------------------------------监控得到的数据 --------------------------------------------
#{u'Iowait': 0.0, u'Idle': 92.69999999999999, u'User': 0.0, u'System': 0.0}
def LinuxCPU(request):
    if request.method == 'POST':
        ReciveData = json.loads(request.body)
            
        ClientIP = ReturnClientIP(request) #获取到客户端的IP地址
        
        try:
            CIP = HWI.HostName.objects.get(HostName = ClientIP)
            HWI.CpuStat.objects.create(CpuIdle= ReciveData['Idle'],CpuIowait=ReciveData['Iowait'],CpuSystem=ReciveData['System'],CpuUser=ReciveData['User'],Host=CIP)
        except Exception,e:
            print e
        
        print 'client ip type is: ',type(ClientIP),'ip is :',ClientIP
        print type(ReciveData),ReciveData
    #return HttpResponse(json.dumps(ReceviedData)) 
    return HttpResponse('ok') 


#{u'lavg_5': u'0.11', u'lavg_15': u'0.19', u'lavg_1': u'0.10'}
def LinuxLoad(request):
    if request.method == 'POST':
        ReciveData = json.loads(request.body)
        print ReciveData
        ClientIP = ReturnClientIP(request)
        CIP=HWI.HostName.objects.get(HostName=ClientIP)
        
        HWI.CpuLoad.objects.create(Load01=ReciveData['lavg_1'],Load05=ReciveData['lavg_5'],Load15=ReciveData['lavg_15'],Host=CIP)

    #return HttpResponse(json.dumps(ReceviedData)) 
    return HttpResponse('ok') 


def DiskUsed(request):
    if request.method == 'POST':
        ReciveData = json.loads(request.body)
        print ReciveData
        ClientIP = ReturnClientIP(request)
        CheckCIP = HWI.HostName.objects.get(HostName=ClientIP)
        
        '''if HWI.DiskInfo.objects.filter(Host_id=CIP.id):
            print "exsit....."
            for for I in ReciveData:
                HWI.DiskInfo.objects.update_or_create()
        else:
# [[u'/dev/mapper/cl-root', u'100G', u'7.2G', u'93G', u'8%', u'/'], [u'devtmpfs', u'3.8G', u'0', u'3.8G', u'0%', u'/dev'], [u'tmpfs', u'3.8G', u'88K', u'3.8G', u'1%', u'/dev/shm'], [u'tmpfs', u'3.8G', u'9.2M', u'3.8G', u'1%', u'/run'], [u'tmpfs', u'3.8G', u'0', u'3.8G', u'0%', u'/sys/fs/cgroup'], [u'/dev/sdb2', u'494M', u'169M', u'326M', u'35%', u'/boot'], [u'/dev/mapper/cl-home', u'50G', u'33M', u'50G', u'1%', u'/home'], [u'/dev/mapper/cl-var', u'50G', u'2.7G', u'48G', u'6%', u'/var'], [u'tmpfs', u'772M', u'52K', u'772M', u'1%', u'/run/user/0']]

            print "no exsit...." '''
        
        if not CheckCIP:
            obj = HWI.HostName.objects.create(HostName=ClientIP)
            print obj
            CIP=HWI.HostName.objects.get(HostName=ClientIP)
        else:
            CIP=HWI.HostName.objects.get(HostName=ClientIP)
            
        for I in ReciveData:
                if I[0] !='tmpfs':
                    #oob = HWI.DiskInfo.objects.update_or_create(FileSystem=I[0],Total=I[1],Used=I[2],Avail=I[3],UseP=I[4],MountedOn=I[5],Host=CIP)                   
                    print I,I[0],I[1]
                    #print type(oob)
                    #oob.hostname_set.add(CIP)
                    #CIP.DiskInfo.add(oob[id])
                    CIP.DiskInfo.update_or_create(FileSystem=I[0],Total=I[1],Used=I[2],Avail=I[3],UseP=I[4],MountedOn=I[5],Host=CIP)                   
           
                    print "DISK"
        
    #return HttpResponse(json.dumps(ReceviedData)) 
    return HttpResponse('ok') 

#{u'Total': 7715, u'Free': 5190}
def MemLoad(request):
    if request.method == 'POST':
        ReciveData = json.loads(request.body)
        #print 'I am  Mem:',ReciveData
        ClientIP = ReturnClientIP(request)
        CIP=HWI.HostName.objects.get(HostName=ClientIP)
        #print CIP
        HWI.MemInfo.objects.create(Total=ReciveData['Total'],Free=ReciveData['Free'],Host=CIP)
        
    #return HttpResponse(json.dumps(ReceviedData)) 
    return HttpResponse('ok') 


#{u'Total': 8191, u'Free': 8191}
def SwapLoad(request):
    if request.method == 'POST':
        ReciveData = json.loads(request.body)
        print 'this is swap',ReciveData
        
        ClientIP = ReturnClientIP(request)
        CIP=HWI.HostName.objects.get(HostName=ClientIP)
        
        HWI.SwapInfo.objects.create(Total=ReciveData['Total'],Free=ReciveData['Free'],Host=CIP)
        
    #return HttpResponse(json.dumps(ReceviedData)) 
    return HttpResponse('ok') 


#{u'System': u'CentOS Linux__7.3.1611', u'CpuLogical': 4, u'Host': u'node1.unull.cn', u'CpuPhysics': 2, u'Arch': u'x86_64__64bit', u'Cpu': u' Intel(R) Core(TM) i5-3337U CPU @ 1.80GHz', u'Mac': u'20:1a:06:e4:a5:9a'}
def HardWareInfo(request):
    if request.method == 'POST':
        ReciveData = json.loads(request.body)
        print 'this is Hwinfo',ReciveData
        
        ClientIP = ReturnClientIP(request)
        #CIP=HWI.HostName.objects.get(HostName=ClientIP)
        CheckCIP = HWI.HostName.objects.filter(HostName=ClientIP)
        
               #先检查HostName是否存在
        
        if not CheckCIP:
            obj = HWI.HostName.objects.create(HostName=ClientIP)
            print obj
            CIP=HWI.HostName.objects.get(HostName=ClientIP)
        else:
            CIP=HWI.HostName.objects.get(HostName=ClientIP)
            
        if HWI.HardInfo.objects.filter(HostName_id=CIP.id):
            print "已经存在"
        else:
           oob =  HWI.HardInfo.objects.update_or_create(Host=ReciveData['Host'],System=ReciveData['System'],Cpulogical=ReciveData['CpuLogical'],Cpupysic=ReciveData['CpuPhysics'],Arch=ReciveData['Arch'],Cpu=ReciveData['Cpu'],Mac=ReciveData['Mac'],HostName=CIP)
           Check = HWI.HardInfo.objects.get(HostName=CIP)
           
           HWI.HostName.objects.filter(HostName=ClientIP).update(HardInfo=Check)
           
           print "ahh"
    return HttpResponse('ok')


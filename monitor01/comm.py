#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####


#GET Client IP_ADDRE
def ReturnClientIP(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        #return request.META['HTTP_X_FORWARDED_FOR']
        print 'HTTP_X_FORWARDED_FOR'
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        #return request.META['REMOTE_ADDR']
        print 'REMOTE_ADDR'
        return request.META['REMOTE_ADDR']
#coding:utf-8
from django.contrib import admin

# Register your models here.
import models
#注册在admin中，使得能直接在admin中修改

class HostAdmin(admin.ModelAdmin):
    list_display = ('id','ip_addr' ,'status')
    
admin.site.register(models.Hosts, HostAdmin) #后一个参数是上面的
admin.site.register(models.HostGroup)
admin.site.register(models.WebAdmin)
admin.site.register(models.Service)
admin.site.register(models.ServiceIndex)
admin.site.register(models.Action)
admin.site.register(models.ActionOperation)
admin.site.register(models.NotifiersUser)
admin.site.register(models.Templates)
admin.site.register(models.Triggers)
admin.site.register(models.Maintenance)

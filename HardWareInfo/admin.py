from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.group)
admin.site.register(models.IDC)
admin.site.register(models.Status)
admin.site.register(models.HardInfo)
admin.site.register(models.DiskInfo)
admin.site.register(models.MemInfo)
admin.site.register(models.NetInOut)
admin.site.register(models.CpuStat)
admin.site.register(models.SwapInfo)
admin.site.register(models.HostName)
admin.site.register(models.CpuLoad)


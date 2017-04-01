"""MikEye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from monitor01 import views
from WebAdmin import views as WA
import HardWareInfo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('monitor01.api_urls')),
    url(r'^HardWareInfo/',include('HardWareInfo.urls')),
    url(r'^stat/',include('monitor01.urls')),
    url(r'^$',WA.Index),
    url(r'^index/$',WA.Index),
    url(r'^Login',WA.Login),
    url(r'^WebAdmin/',include('WebAdmin.urls')),
    #url(r'.*',views.ClientError),
]

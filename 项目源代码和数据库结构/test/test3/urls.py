#作者：王皓平、仲银炜 创建时间：2019.8.22 最后修改时间：2019.9.10
"""test3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('LogReg/', include('LogReg.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from login import views
from mainWindow import views_mainWindow

urlpatterns = [
   # url('admin/', admin.site.urls),
    #url(r'^$', views.index),
    #url(r'regist/$', views.regist),
    #url(r'login/$', views.login),
    #url(r'logout/$', views.logout),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^information/', views.information),
    url(r'^edit/', views.edit),
    url(r'^captcha', include('captcha.urls')),
    url(r'^userInfo/', views.userInfo),
    #url(r'article/$', views.article),
    #url(r'(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'index1', views_mainWindow.index1),
    url(r'indexnj', views_mainWindow.indexnj),
    url(r'indexbj', views_mainWindow.indexbj),
    url(r'indextj', views_mainWindow.indextj),
    url(r'indexsh', views_mainWindow.indexsh),
    url(r'indexhz', views_mainWindow.indexhz),
    url(r'indexcd', views_mainWindow.indexcd),
    url(r'indexcs', views_mainWindow.indexcs),
    url(r'indexsz', views_mainWindow.indexsz),
    url(r'indexty', views_mainWindow.indexty),
    url(r'indexnc', views_mainWindow.indexnc),
    url(r'indexsu', views_mainWindow.indexsu),
    url(r'indexwx', views_mainWindow.indexwx),
    url(r'indexwh', views_mainWindow.indexwh),
    url(r'indexgz', views_mainWindow.indexgz),
    url(r'result1', views_mainWindow.search),
    url(r'predict', views_mainWindow.predict),
    url(r'result2', views_mainWindow.houseSelect),
    url(r'compare', views.Hcompare),
]

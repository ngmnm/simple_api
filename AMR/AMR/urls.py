
from django.contrib import admin
from django.urls import path, include, URLPattern
from api.views import VenderView, VenderViewAll, DeviceModelView, DeviceModelViewAll 
from django.conf.urls import url

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
    url(r'^vender/(?P<pk>\d+)/$' ,VenderView.as_view(), name="vender"),
    url(r'^vender', VenderViewAll.as_view(), name="venderAll"),
    url(r'^device/(?P<pk>\d+)/$', DeviceModelView.as_view(), name="device"),
    url(r'^device', DeviceModelViewAll.as_view(), name="deviceAll"),


]

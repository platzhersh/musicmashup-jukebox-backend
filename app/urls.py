# TODO: fix package names
"""websockets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from api import urls as api_urls
from frontend import views as frontend_views


urlpatterns = [
	url(r'^$', frontend_views.home, name='home'),
	url(r'^rooms/$', frontend_views.rooms, name='rooms'),
	url(r'^rooms/(?P<pk>[0-9]+)/?$', frontend_views.room, name="room"),
	url(r'^api/', include(api_urls, namespace="api")),
    url(r'^admin/', admin.site.urls),
]
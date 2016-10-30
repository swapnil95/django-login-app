"""Myapp URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views, urls as auth_urls
from social.apps.django_app import urls as social_auth_urls

from api import urls as api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include(auth_urls, namespace='auth')),
    url('', include(social_auth_urls, namespace='social')),
    url(r'^api/', include(api_urls)),
]

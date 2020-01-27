"""contatoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import handler404, handler500
from contatoapp import views
from contatoapp import views as myapp_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^contato', views.contato, name='contato'),
]

#http://thepythondjango.com/designing-custom-404-500-error-pages-django/
handler404 = myapp_views.error_404
handler500 = myapp_views.error_500
handler502 = myapp_views.error_502

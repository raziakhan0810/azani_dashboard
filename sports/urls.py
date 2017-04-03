"""sports URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from sports_products.views import *

urlpatterns = [

    url(r'^$', home_page),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', register, name='register'),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^order/', create_order, name='order'),
]

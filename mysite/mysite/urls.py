"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns,url,include
#from django.conf.urls import *
from views import *
from books.views import *

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]
urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        (r'^search/$', search),
        (r'^main/$', main),
        (r'^bookmessage/$', bookmessage),
        (r'^add/$', add),
        (r'^update/$', update),
        (r'^allbooks/$', allbooks),
        (r'^delete/$', delete),
        (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'd:/mysite/books/static'}),  
        #(r'^search-form/$', search_form),
)
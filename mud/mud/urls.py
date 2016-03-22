from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.indx, name='indx'),
    url(r'^$about.html/', views.index, name='about'),

]
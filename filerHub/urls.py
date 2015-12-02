from django.conf.urls import url
from filerHub import views

urlpatterns =[
    url(r'^form/$', views.form),
    url(r'^upload/$', views.upload),
]

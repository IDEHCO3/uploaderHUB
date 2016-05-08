from django.conf.urls import url
from filerHub_api import views

urlpatterns =[
  url(r'^files', views.FileUploadView.as_view()),
  url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectCollectorDetail.as_view(), name='uf_detail_id_objeto'),
  url(r'^projects/$', views.ProjectCollectorList.as_view()),




]

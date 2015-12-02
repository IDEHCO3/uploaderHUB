from django.conf.urls import url
from filerHub_api import views

urlpatterns =[
  url(r'^', views.FileUploadView.as_view()),
]

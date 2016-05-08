from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response

from filerHub_api.models import ProjectCollector
from filerHub_api.serializers import ProjectCollectorSerializer
from uploaderHUB import settings
from rest_framework import generics



class ProjectCollectorList(generics.ListCreateAPIView):
    queryset = ProjectCollector.objects.all()
    serializer_class = ProjectCollectorSerializer

class ProjectCollectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectCollector.objects.all()
    serializer_class = ProjectCollectorSerializer


class FileUploadView(views.APIView):
   parser_classes = (MultiPartParser,FileUploadParser)


   #def default_response_headers(self):
   #   self.headers['Location'] = 'http://172.17.42.1:8001/media'

   #   return super(FileUploadView, self).default_response_headers()

   def get(self, request, format=None):
      if request.method == 'HEAD':
         dic_headers = {}
         dic_headers['Location'] = 'http://192.168.56.1:8000/files/'
         return Response(status=204, content_type='multipart/form-data', headers=dic_headers)

      uploaded_files = FileUpload.objects.all()
      serializer = FileUploadSerializer(uploaded_files, many=True)
      res = Response(serializer.data)
      return res


   def put(self, request, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=201)

   def post(self, request, format=None):
        #a_file = request.FILES.getlist('xml_submission_file')[0]
        a_file = request.FILES.getlist('files')[0]
        handle_uploaded_file(a_file)
        #dic_headers = {}
        #dic_headers['Location'] = 'http://192.168.56.1:8000/files' + a_file._name
        #return Response(status=201)
        return Response("File(s) uploaded!", status=201)


def handle_uploaded_file(file):
            with open(settings.MEDIA_ROOT + '/' + file._name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)


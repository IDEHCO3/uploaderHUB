from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from uploaderHUB import settings
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
#from probably.obtain.models import FileUpload
#from probably.obtain.serializers import FileUploadSerializer

"""
class FileUploadViewSet(ModelViewSet):

    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       datafile=self.request.data.get('datafile'))
"""
def form(request):
    return render(request, 'fileHub/form.html', {})

def upload(request):
    for a_file in request.FILES.getlist("files"):
        handle_uploaded_file(a_file)
    return HttpResponse("File(s) uploaded!")


def handle_uploaded_file(file):
            with open(settings.MEDIA_ROOT + '/' + file._name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

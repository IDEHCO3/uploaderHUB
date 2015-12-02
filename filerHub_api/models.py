from django.contrib.auth.models import User
from django.db import models
#from probably.users.models import User

class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, to_field='id')
    datafile = models.FileField()

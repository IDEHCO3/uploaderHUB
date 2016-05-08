from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models
#from probably.users.models import User
from django_pgjson.fields import JsonBField

class ProjectCollector(models.Model):

    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)


class CollectedData(models.Model):

    properties = JsonBField()  # can pass attributes like null, blank, ecc.
    geom = models.GeometryField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    project_collector = models.ForeignKey(ProjectCollector)






# serializers.py
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from filerHub_api.models import ProjectCollector


class ProjectCollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCollector
        fields = ['id', 'name', 'date_created' ]



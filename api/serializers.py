from rest_framework import serializers
from .models import seodata


class seodataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seodata
        fields = ('id', 'url', 'name', 'language', 'price')

from rest_framework import serializers
from .models import seodata, urlindex


class seodataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seodata
        fields = ('id', 'url', 'name', 'language', 'price')


class urlindexserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = urlindex
        fields = ('id', 'url')

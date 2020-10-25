from django.shortcuts import render
from rest_framework import viewsets
from .models import seodata
from .serializers import seodataserializer


class projectview(viewsets.ModelViewSet):
    queryset = seodata.objects.all()
    serializer_class = seodataserializer

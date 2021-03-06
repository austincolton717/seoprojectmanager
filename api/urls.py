from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('seodata', views.projectview)
router.register('urlindex', views.projectview)

urlpatterns = [
    path('', include(router.urls)),
]

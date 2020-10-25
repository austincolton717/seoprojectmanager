from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homesite.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('api/', include('api.urls')),

]

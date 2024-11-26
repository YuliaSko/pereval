from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_pereval import views
from .yasg import urlpatterns as doc_urls

router = routers.SimpleRouter()
router.register(r'pereval', views.PerevalViewSet, basename='pereval')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += doc_urls

from django import views
from django.urls import path, include
from .views import BlogViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
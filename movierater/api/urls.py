from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet, RatingViewSet, UserVIewSet

router = routers.DefaultRouter()
router.register('users',UserVIewSet)
router.register('movies', MovieViewSet)
router.register('ratings',RatingViewSet)

urlpatterns = [
    path('',include(router.urls))

]
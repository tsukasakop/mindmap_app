from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('user', views.CustomUserViewSet)
router.register('mindmap', views.MindMapViewSet)
router.register('topic', views.TopicViewSet)

urlpatterns = [path("", include(router.urls))]

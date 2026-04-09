from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, ContentDetailView, LatestVersionView, VersionListView

app_name = 'api'

router = DefaultRouter()
router.register(r'items', ContentViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls)),

    path('item/<slug:slug>/', ContentDetailView.as_view(), name='item-detail'),
    path('item/<slug:slug>/latest/', LatestVersionView.as_view()),
    path('item/<slug:slug>/versions/', VersionListView.as_view()),
]
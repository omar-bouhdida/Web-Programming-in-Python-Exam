from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageContentViewSet, generate_preview_token, public_content_stats

router = DefaultRouter()
router.register(r'content', PageContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('content/<int:pk>/generate-preview-token/', generate_preview_token),
    path('public/', public_content_stats, name='public_content_stats'),
]
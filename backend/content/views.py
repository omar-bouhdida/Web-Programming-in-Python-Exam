from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404
from django.db import models
from .models import PageContent
from .serializers import (
    PageContentSerializer,
    PageContentListSerializer,
    PageContentPreviewSerializer,
    CreatePageContentSerializer,
    UpdatePageContentSerializer
)
import secrets
from django.utils import timezone

# In-memory token store (for demo purposes)
PREVIEW_TOKENS = {}

class PageContentViewSet(viewsets.ModelViewSet):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = PageContent.objects.all()
        if self.action == 'list':
            # Show only published content for non-authenticated users
            if not self.request.user.is_authenticated:
                queryset = queryset.filter(is_published=True, publish_date__lte=timezone.now())
            # For authenticated users, show their own content + published content
            elif not hasattr(self.request.user, 'role') or self.request.user.role not in ['admin', 'editor']:
                queryset = queryset.filter(
                    models.Q(author=self.request.user) | 
                    models.Q(is_published=True, publish_date__lte=timezone.now())
                )
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PageContentListSerializer
        if self.action == 'create':
            return CreatePageContentSerializer
        if self.action in ['update', 'partial_update']:
            return UpdatePageContentSerializer
        return PageContentSerializer

    @action(detail=True, methods=['get'], url_path='preview/(?P<token>[^/.]+)')
    def preview(self, request, pk=None, token=None):
        content = get_object_or_404(PageContent, pk=pk)
        if PREVIEW_TOKENS.get(token) == str(pk):
            serializer = PageContentPreviewSerializer(content)
            return Response(serializer.data)
        return Response({'detail': 'Invalid or expired token'}, status=403)

@api_view(['POST'])
def generate_preview_token(request, pk):
    token = secrets.token_urlsafe(16)
    PREVIEW_TOKENS[token] = str(pk)
    return Response({'token': token})


@api_view(['GET'])
@permission_classes([AllowAny])
def public_content_stats(request):
    """Public endpoint for homepage stats"""
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    total_content = PageContent.objects.filter(is_published=True).count()
    total_users = User.objects.filter(is_active=True).count()
    recent_content = PageContent.objects.filter(
        is_published=True, 
        publish_date__lte=timezone.now()
    ).select_related('author').order_by('-publish_date')[:6]
    
    recent_content_data = []
    for content in recent_content:
        # Handle null author
        author_data = None
        if content.author:
            author_data = {
                'username': content.author.username,
                'first_name': content.author.first_name,
                'last_name': content.author.last_name,
            }
        
        recent_content_data.append({
            'id': content.id,
            'title': content.title,
            'content': content.body[:200] + '...' if len(content.body) > 200 else content.body,
            'content_type': getattr(content, 'content_type', 'article'),
            'author': author_data,
            'created_at': content.created_at.isoformat() if content.created_at else None,
            'meta_description': getattr(content, 'meta_description', ''),
        })
    
    return Response({
        'total_content': total_content,
        'total_users': total_users,
        'recent_content': recent_content_data,
    })
import re
from rest_framework import serializers
from .models import PageContent

class PageContentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_details = serializers.SerializerMethodField()
    
    class Meta:
        model = PageContent
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'updated_at')
    
    def get_author_details(self, obj):
        return {
            'id': obj.author.id,
            'username': obj.author.username,
            'first_name': obj.author.first_name,
            'last_name': obj.author.last_name,
        }

class PageContentListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = PageContent
        fields = ['id', 'title', 'slug', 'content_type', 'publish_date', 'is_published', 'author', 'created_at']

class PageContentPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['title', 'body', 'slug', 'meta_description']

class CreatePageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['title', 'body', 'content_type', 'meta_description', 'publish_date', 'is_published']

    def validate(self, data):
        # Example of extra validation
        if data.get('is_published') and not data.get('publish_date'):
            raise serializers.ValidationError("Published content must have a publish date.")
        return data

class UpdatePageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['title', 'body', 'content_type', 'meta_description', 'publish_date', 'is_published']

def validate_slug(self, value):
    if not re.match(r'^[a-z0-9-]+$', value):
        raise serializers.ValidationError("Slug must contain only lowercase letters, numbers, and hyphens.")
    return value
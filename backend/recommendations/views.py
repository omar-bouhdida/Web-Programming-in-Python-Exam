from rest_framework.decorators import api_view
from rest_framework.response import Response
from content.serializers import PageContentListSerializer
from .services import get_recommendations_for

@api_view(['GET'])
def get_recommendations(request, slug):
    recommended = get_recommendations_for(slug)
    serializer = PageContentListSerializer(recommended, many=True)
    return Response(serializer.data)
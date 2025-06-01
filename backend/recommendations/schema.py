import graphene
from graphene_django.types import DjangoObjectType
from content.models import PageContent
from .services import get_recommendations_for

class RecommendationType(DjangoObjectType):
    class Meta:
        model = PageContent

class RecommendationQuery(graphene.ObjectType):
    recommendations = graphene.List(RecommendationType, slug=graphene.String(required=True))

    def resolve_recommendations(self, info, slug):
        return get_recommendations_for(slug)
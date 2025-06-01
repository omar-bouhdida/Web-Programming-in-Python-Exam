import graphene
from graphene_django.types import DjangoObjectType
from .models import PageContent
from django.utils import timezone
from django.utils.text import slugify

class PageContentType(DjangoObjectType):
    class Meta:
        model = PageContent
        fields = "__all__"

class CreatePageContent(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        content_type = graphene.String()
        meta_description = graphene.String()
        is_published = graphene.Boolean()

    page_content = graphene.Field(PageContentType)

    def mutate(self, info, title, body, content_type="article", meta_description="", is_published=False):
        # Generate slug from title
        slug = slugify(title)
        
        # Ensure unique slug
        counter = 1
        original_slug = slug
        while PageContent.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1

        page_content = PageContent.objects.create(
            title=title,
            slug=slug,
            body=body,
            content_type=content_type,
            meta_description=meta_description,
            is_published=is_published,
            publish_date=timezone.now() if is_published else None,
            author=info.context.user if info.context.user.is_authenticated else None
        )
        
        return CreatePageContent(page_content=page_content)

class UpdatePageContent(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        body = graphene.String()
        content_type = graphene.String()
        meta_description = graphene.String()
        is_published = graphene.Boolean()

    page_content = graphene.Field(PageContentType)

    def mutate(self, info, id, **kwargs):
        try:
            page_content = PageContent.objects.get(id=id)
            
            # Update fields if provided
            for field, value in kwargs.items():
                if value is not None:
                    setattr(page_content, field, value)
            
            # Update publish_date if publishing
            if kwargs.get('is_published') and not page_content.publish_date:
                page_content.publish_date = timezone.now()
            
            page_content.save()
            return UpdatePageContent(page_content=page_content)
        except PageContent.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):
    create_page_content = CreatePageContent.Field()
    update_page_content = UpdatePageContent.Field()

class Query(graphene.ObjectType):
    page_content = graphene.Field(PageContentType, id=graphene.Int())
    page_content_by_slug = graphene.Field(PageContentType, slug=graphene.String(required=True))
    all_page_contents = graphene.List(PageContentType)

    def resolve_page_content(self, info, id):
        return PageContent.objects.filter(id=id, is_published=True, publish_date__lte=timezone.now()).first()

    def resolve_page_content_by_slug(self, info, slug):
        return PageContent.objects.filter(slug=slug, is_published=True, publish_date__lte=timezone.now()).first()

    def resolve_all_page_contents(self, info):
        return PageContent.objects.filter(is_published=True, publish_date__lte=timezone.now())

schema = graphene.Schema(query=Query, mutation=Mutation)
from django.core.management.base import BaseCommand
from django.utils import timezone
from content.models import PageContent
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create sample page content for testing'

    def handle(self, *args, **options):
        # Clear existing content
        PageContent.objects.all().delete()
        
        sample_contents = [
            {
                'title': 'Welcome to Our Platform',
                'body': '''Welcome to our amazing content management platform! 

This platform allows you to create, manage, and publish content seamlessly. Whether you're writing blog posts, creating landing pages, or managing documentation, our system provides all the tools you need.

Key features include:
- Easy content creation and editing
- Automatic slug generation
- Publishing controls with scheduled publishing
- GraphQL API for flexible data access
- Modern React frontend

We hope you enjoy using our platform and look forward to seeing what amazing content you'll create!''',
                'is_published': True,
                'publish_date': timezone.now() - timedelta(days=5)
            },
            {
                'title': 'Getting Started Guide',
                'body': '''Getting started with our platform is easy! Here's a step-by-step guide to help you begin:

## Step 1: Understanding Content
Content in our system consists of a title, body text, and metadata like publication status and dates.

## Step 2: Creating Content
Use the Django admin interface to create new content. You can write in plain text or use basic formatting.

## Step 3: Managing Publication
Set the publication status and date to control when your content goes live. Published content with future dates won't appear until that date arrives.

## Step 4: Accessing Content
Use our GraphQL API or the React frontend to access and display your content.

## Tips for Success
- Write clear, engaging titles
- Use proper formatting for readability
- Schedule content for optimal timing
- Review content before publishing

That's it! You're ready to start creating amazing content.''',
                'is_published': True,
                'publish_date': timezone.now() - timedelta(days=3)
            },
            {
                'title': 'API Documentation',
                'body': '''Our platform provides a powerful GraphQL API for accessing content programmatically.

## Available Queries

### Get All Content
Query all published content with the `allPageContents` field.

### Get Content by Slug
Retrieve specific content using the `pageContentBySlug` query.

### Get Content by ID
Access content directly by ID using the `pageContent` query.

## Content Fields
- id: Unique identifier
- title: Content title
- slug: URL-friendly identifier
- body: Main content text
- publishDate: When the content was/will be published
- isPublished: Publication status

## GraphQL Endpoint
Access the API at `/graphql/` with GraphiQL interface enabled for testing.

## Authentication
Currently, the API is open for reading. Authentication may be added for content management operations.

For more detailed examples and advanced usage, refer to our technical documentation.''',
                'is_published': True,
                'publish_date': timezone.now() - timedelta(days=1)
            },
            {
                'title': 'Future Features Roadmap',
                'body': '''We're constantly working to improve our platform. Here's what's coming next:

## Content Management Enhancements
- Rich text editor with WYSIWYG capabilities
- Image and media upload support
- Content versioning and revision history
- Content categories and tagging

## User Experience Improvements
- Enhanced search functionality
- Content filtering and sorting options
- Responsive design improvements
- Dark mode support

## Developer Features
- REST API endpoints alongside GraphQL
- Webhook support for content events
- Advanced caching strategies
- Content delivery network integration

## Security and Performance
- Enhanced authentication and authorization
- Content moderation tools
- Performance monitoring and optimization
- Security audit and improvements

## Timeline
We aim to release these features incrementally over the coming months. Stay tuned for updates!

Have suggestions for new features? We'd love to hear from you!''',
                'is_published': True,
                'publish_date': timezone.now()
            },
            {
                'title': 'Draft: Upcoming Announcement',
                'body': '''This is a draft post that hasn't been published yet.

It contains information about an upcoming major announcement that we're not ready to share publicly.

The content here is still being refined and reviewed before publication.''',
                'is_published': False,
                'publish_date': None
            }
        ]

        created_count = 0
        for content_data in sample_contents:
            content = PageContent(**content_data)
            content.save()
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Created content: "{content.title}"')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample content entries')
        )

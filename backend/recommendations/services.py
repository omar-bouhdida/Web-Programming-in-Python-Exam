from content.models import PageContent

def get_recommendations_for(slug):
    try:
        content = PageContent.objects.get(slug=slug)
    except PageContent.DoesNotExist:
        return []

    # Mock logic: return other published pages with shared words in title
    words = set(content.title.lower().split())
    recommendations = []

    for item in PageContent.objects.exclude(slug=slug).filter(is_published=True):
        if words.intersection(set(item.title.lower().split())):
            recommendations.append(item)

    return recommendations[:5]  # return top 5 for example
from celery import shared_task

@shared_task
def regenerate_static_page(slug):
    print(f"[CELERY] Triggering static regeneration for slug: {slug}")
    # You can make a call to Next.js (e.g., revalidate tag or API call to rebuild)
    # Example: call Next.js preview webhook or API endpoint
from django.urls import path
from .views import get_recommendations

urlpatterns = [
    path('<slug:slug>/', get_recommendations, name='get_recommendations'),
]
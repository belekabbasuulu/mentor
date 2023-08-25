from django.urls import path

from .views import (
    AdsListView,
    AdsDetailView,
    AdsUpdateView,
    AdsDeleteView,
    category_list,
    AdsCreateView,
)


urlpatterns = [
    path("", AdsListView.as_view(), name="ads-list"),
    path("category", category_list, name="category-list"),
    path('create', AdsCreateView.as_view(), name='create_ad'),
    path('update/<int:pk>/', AdsUpdateView.as_view(), name='update_ad'),
    path('<int:pk>/', AdsDetailView.as_view(), name='retrieve_ad'),
    path('delete/<int:pk>', AdsDeleteView.as_view(), name='delete_ad')
]
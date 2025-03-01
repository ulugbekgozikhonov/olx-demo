from django.urls import path

from .views import CategoryListView, AdvertisementCreateView, UserProfileCreateView, AdvertisementDetailView, AdvertisementListView, AdvertisementSearchView

app_name = 'products'

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('advertisements/<int:category_id>', AdvertisementListView.as_view(), name='advertisements'),
    path('advertisement/', AdvertisementCreateView.as_view(), name='advertisement'),
    path('advertisement/<int:id>', AdvertisementDetailView.as_view(), name='detail_ads'),
    path('profile/', UserProfileCreateView.as_view(), name='profile'),
    # path('single/', ProductListView.as_view(), name='single'),
    path("search/", AdvertisementSearchView.as_view(), name="advertisement_search"),
]
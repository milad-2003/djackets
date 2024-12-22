from django.urls import path, include

from .views import *


urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
]

from django.urls import path, include

from .views import *


urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
]

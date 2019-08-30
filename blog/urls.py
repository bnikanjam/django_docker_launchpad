from django.urls import path

from .views_api import PostAPIList, PostAPIDetail

urlpatterns = [
    # ex: blog/api/v1/
    path('api/v1/', PostAPIList.as_view()),
    # ex: blog/api/v1/ab-testing/
    path('api/v1/<slug:slug>/', PostAPIDetail.as_view()),
]

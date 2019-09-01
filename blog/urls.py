from django.urls import path, include

from .views_api import PostAPIList, PostAPIDetail

urlpatterns = [
    # ex: blog/api/v1/
    path('api/v1/', PostAPIList.as_view()),
    # ex: blog/api/v1/ab-testing/
    path('api/v1/<slug:slug>/', PostAPIDetail.as_view()),

    path('api/v1/rest-auth/', include('rest_auth.urls')),  # login, logout, password reset endpoints
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]

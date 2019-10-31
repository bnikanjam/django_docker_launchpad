from django.urls import path, include

from .views_api import PostAPIList, PostAPIDetail
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import post_email

urlpatterns = [
    # ex: blog/new/
    path('new/', PostCreateView.as_view(), name='post-create'),
    # ex: blog/title/
    # TODO blog/author/date/title i.e. blog/babak/2019-september/ab-testing
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    # ex: blog/
    path('', PostListView.as_view(), name='post-list'),
    # ex: blog/title/update/
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    # ex: blog/title/delete/
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # ex: blog/title/email/
    path('<slug:slug>/email/', post_email, name='post-email'),

    # ex: blog/api/v1/
    path('api/v1/', PostAPIList.as_view()),
    # ex: blog/api/v1/ab-testing/
    path('api/v1/<slug:slug>/', PostAPIDetail.as_view()),

    path('api/v1/rest-auth/', include('rest_auth.urls')),  # login, logout, password reset endpoints
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]

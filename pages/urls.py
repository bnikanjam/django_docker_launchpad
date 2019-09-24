from django.urls import path

from pages.views import HomePageView, DownloadResumeView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('resume/', DownloadResumeView.as_view(), name='resume'),
]

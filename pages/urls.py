from django.urls import path

from pages.views import HomePageView, ContactMeView


urlpatterns = [
    path('', HomePageView.as_view(), name='cover'),
    path('contact-babak/', ContactMeView.as_view(), name='contactme'),
]

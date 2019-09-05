from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'coverhome.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactMeView(TemplateView):
    template_name = 'contactme.html'

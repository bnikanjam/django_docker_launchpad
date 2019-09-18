from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'coverhome.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class DownloadResumeView(LoginRequiredMixin, TemplateView):
    template_name = 'resume.html'

from django.shortcuts import render
from django.views import generic

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "homepage.html"


class BlogPage(generic.TemplateView):
    template_name = "blogpage.html"


class TestmonialPage(generic.TemplateView):
    template_name = "testmonialpage.html"


from typing import Any
from django.shortcuts import redirect, render

from django.views.generic import ListView, TemplateView
class IndexView(TemplateView):
    template_name= "index.html"


class AboutView(TemplateView):
    template_name= "about.html"

class AnalysisView(TemplateView):
    template_name= "analysis.html"

class BlogView(TemplateView):
    template_name= "blog.html"

class ContactView(TemplateView):
    template_name= "input.html"




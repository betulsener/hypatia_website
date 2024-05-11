from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView
from tcore.models import Slider, About

class IndexView(ListView):
    template_name= "index.html"
    model = Slider


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Sliders'] = Slider.objects.all()
        context['Abouts'] = About.objects.first()

        return context
        
    
class AboutView(ListView):
    template_name= "about.html"
    context_object_name="Abouts"
    queryset=About.objects.first()

class AnalysisView(TemplateView):
    template_name= "analysis.html"

class BlogView(TemplateView):
    template_name= "blog.html"

class ContactView(TemplateView):
    template_name= "input.html"


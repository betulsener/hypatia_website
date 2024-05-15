from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from tcore.models import Slider, About, Input
from django.contrib import messages

class IndexView(ListView):
    template_name= "index.html"
    model = Slider


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Sliders'] = Slider.objects.all()
        context['Abouts'] = About.objects.first()
        context['Inputs'] = Input.objects.all()

        return context
    
class BaseView(object):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['PBlogs']=Input.objects.order_by('-views')[:5]
        return context
        
    
class AboutView(ListView):
    template_name= "about.html"
    context_object_name="Abouts"
    queryset=About.objects.first()

class AnalysisView(TemplateView):
    template_name= "analysis.html"

class BlogView(BaseView, ListView):
    template_name= "blog.html"
    context_object_name = "Inputs"
    queryset = Input.objects.all()

class BlogDetailView(BaseView, DetailView):
    model = Input
    template_name = "blog-details.html"
    context_object_name = "input"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views+=1
        obj.save()
        return obj


class ContactView(TemplateView):
    template_name= "input.html"
    def post(self, request, *args, **kwargs):
        full_name = request.POST.get('fullName')
        job = request.POST.get('job')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')

        try:
            input_instance = Input.objects.create(
                full_name=full_name,
                job=job,
                email=email,
                title=title,
                message=message
            )
            messages.success(request,'İletiniz başarıyla gönderildi.')

        except Exception as e:
            messages.error(request, f'Mesaj gönderimi başarısız oldu: {e}')

        return HttpResponseRedirect(reverse('input'))




from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from tcore.models import Slider, About, Input
from django.contrib import messages
from taggit.models import Tag
from django.db.models import Count

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
        context['most_common_tags'] = Tag.objects.annotate(num_times=Count('taggit_taggeditem_items')).order_by('-num_times')[:5]

        return context
        
    
class AboutView(ListView):
    template_name= "about.html"
    context_object_name="Abouts"
    queryset=About.objects.first()

class TagDetailView(ListView):
    template_name = 'tag-details.html'
    context_object_name = 'Inputs'

    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        return Input.objects.filter(tags__name__in=[tag_name])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_name')
        return context

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
        tags = request.POST.get('tags')

        try:
            input_instance = Input.objects.create(
                full_name=full_name,
                job=job,
                email=email,
                title=title,
                message=message

            )

            if tags:
                tag_list = [tag.strip() for tag in tags.split(',')]
                input_instance.tags.add(*tag_list)

            messages.success(request,'İletiniz başarıyla gönderildi.')

        except Exception as e:
            messages.error(request, f'Mesaj gönderimi başarısız oldu: {e}')

        return HttpResponseRedirect(reverse('input'))




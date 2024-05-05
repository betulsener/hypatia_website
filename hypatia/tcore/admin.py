from django.contrib import admin
from .models import About, Input, Analysis
from modeltranslation.admin import TranslationAdmin


@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display=('full_name','email','job','title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title',)

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display=('title',)
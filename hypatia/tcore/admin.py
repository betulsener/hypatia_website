from django.contrib import admin
from .models import About, Input, Analysis, Slider, Category, Blog, Setting
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

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('title', 'image', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'views', 'created', 'update', )

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display=('title',)
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
     
    

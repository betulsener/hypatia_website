from django.contrib import admin
from .models import About, Input, Analysis, Slider, Category, Setting
from modeltranslation.admin import TranslationAdmin




@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display=('full_name','email','job','title','views', 'created_at',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title',)
    group_fieldsets = True

    class Media:
        js = (
            
            'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
            )
        
        css = {
            'all':
            ('modeltranslation/css/tabbed_translation_fields.css',)
            }

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


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display=('title',)
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
     
    

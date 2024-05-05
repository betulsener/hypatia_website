from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Input(models.Model):
    full_name=models.CharField(max_length=100, verbose_name="Ad Soyad")
    job=models.CharField(max_length=100, verbose_name="Meslek")
    email=models.EmailField()
    title=models.CharField(max_length=100, verbose_name="Başlık")
    message=models.TextField(verbose_name="İleti")

class About(models.Model):
    title=models.CharField(max_length=200, verbose_name="Başlık")
    content=RichTextField(verbose_name="İçerik")

class Analysis(models.Model):
    title=models.CharField(max_length=200, verbose_name="Başlık")
    content=RichTextField(verbose_name="İçerik")
    slug=models.SlugField(max_length=200, blank=True, editable=False)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Analysis,self).save(*args, **kwargs)

class Slider(models.Model):
    title=models.CharField(max_length=200, verbose_name="Başlık")
    image=models.ImageField(upload_to='slider', verbose_name="Görsel")

class Category(models.Model):
    name=models.CharField(max_length=200, verbose_name="İsim")
    slug=models.SlugField(max_length=100, unique=True, blank=True, editable=False)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200, verbose_name="Başlık")
    image=models.ImageField(upload_to='blog', verbose_name="Görsel")
    content=RichTextField(verbose_name="İçerik")
    category=models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")
    views=models.IntegerField(default=0, verbose_name="Görüntülenme Sayısı")
    slug=models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    update=models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Blog,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Setting(models.Model):
    logo_1 = models.ImageField(upload_to='dimg', null=True, blank=True)
    logo_2 = models.ImageField(upload_to='dimg', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Başlık")
    description = models.CharField(max_length=255, verbose_name="Açıklama")
    keywords = models.CharField(max_length=255, verbose_name="Anahtar kelimeler")
    phone = models.CharField(max_length=15, verbose_name="Telefon numarası")
    address=models.TextField(verbose_name="Adres")
    mail = models.EmailField(verbose_name="Mail adresi")
    other_url=models.URLField(max_length=255, verbose_name="Resmi web sitesi")





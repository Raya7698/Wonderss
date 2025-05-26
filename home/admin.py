from django.contrib import admin
from home.models import Blog, Main, AboutUs, Gallery, ContactUs, Comments, PhotoGallery


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['site_name']

@admin.register(Blog)
class HomeAdmin(admin.ModelAdmin):
    list_display = [ 'photo', 'title', 'description', 'created_at']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['photo', 'title', 'description']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(ContactUs)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['full_name']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','post']


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['photo']




# Register your models here.

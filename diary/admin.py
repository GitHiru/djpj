from django.contrib import admin
from diary.models import Category, Tag, Post, ContentImage

class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines            = [ContentImageInline,]
    list_display       = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_public')
    list_display_links = ('id', 'title')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'timestamp')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'timestamp')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

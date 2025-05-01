from django.contrib import admin
from .models import Page, Config, Post, Category, Tags, Image, HomePage

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('categories', 'tags')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags', 'categories')
    inlines = [ImageInline]

# Registra los demás modelos igual que antes
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('order', 'created_at')
    filter_horizontal = ('posts', )

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'created_at', 'updated_at')
    search_fields = ('site_name', 'site_description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'created_at')
    search_fields = ('post__title',)
    readonly_fields = ('created_at',)
    list_filter = ('post',)
    ordering = ('-created_at',)

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-created_at',)
    filter_horizontal = ('posts', )

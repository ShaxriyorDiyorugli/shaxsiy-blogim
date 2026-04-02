from django.contrib import admin
from .models import Post, Category, Comment

class Admin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'title', 'created_at', 'is_publish', )
    list_editable = ('is_publish',)
    list_display_links = ('title', 'category')
    list_filter = ('title', 'created_at')

admin.site.register(Category)
admin.site.register(Post, Admin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Comment, CommentAdmin)
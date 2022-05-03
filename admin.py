from curses import raw
from django.contrib import admin

from .models import Faq, Inquiry, Answer

class CommentInline(admin.TabularInline):
    model = Answer
    extra = 1

# Register your models here.

@admin.register(Faq)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_by')
    search_fields = ['title']
    list_filter = ['category']

admin.site.register(Inquiry)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_at', 'created_at')
    search_fields = ['title', 'email', 'phone']
    list_filter = ['category']
    inlines = [Answer]

admin.site.register(Answer)

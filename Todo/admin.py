from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'completed', 'created_at')  
    list_filter = ('created_at',)

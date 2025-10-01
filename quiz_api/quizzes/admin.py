from django.contrib import admin
from .models import Quiz

# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')  
    search_fields = ('title', 'description')  
    list_filter = ('created_at',)  

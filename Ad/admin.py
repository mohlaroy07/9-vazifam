from django.contrib import admin

from .models import Category, AdImage


class AdImageInline(admin.StackedInline):
    model = AdImage
    fields = ["image"]
    max_num = 3
    
    
admin.site.register(Category)

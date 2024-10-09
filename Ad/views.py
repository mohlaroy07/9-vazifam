from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from .models import Ad, Category
from .forms import AdForm

def home_page(request):
    all_ads = Ad.objects.all()
    ads = Ad.objects.all()
    
    categories = Category.objects.all()
    context = {
        "ads": ads,
        "categories": categories,
        "all_ads": all_ads
    }
    
    return render(request, "index.html", context)
from django.shortcuts import render
from productApp.models import *
# Create your views here.


def index(request):
    audio = Category.objects.get(title="Audio")
    audio_products = Product.objects.filter(category_id=audio.id)
    categories = Category.objects.all()
    context = {"categories": categories,
               "audio_products": audio_products}
    return render(request, 'index.html', context)

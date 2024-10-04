from django.shortcuts import render
from .models import Fragrance


def collection_manager(request):
    fragrances = Fragrance.objects.all()
    return render(request, 'collection/collection_manager.html', {
        'fragrances' : fragrances
    })

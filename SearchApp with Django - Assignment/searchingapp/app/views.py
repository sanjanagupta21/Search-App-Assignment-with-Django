
from django.shortcuts import render
from .models import Dish
from .forms import DishSearchForm
from django.db.models import Q

def dish_search_view(request):
    form = DishSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Dish.objects.filter(
            Q(name__icontains=query)
        )

    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'dish_search.html', context)

def home_view(request):
    return render(request, 'home.html')


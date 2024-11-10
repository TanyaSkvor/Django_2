from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def home_view(request):
    recipe = DATA.keys()
    return HttpResponse('<br>'.join(recipe))

def cooking_view(request, recipe):
    recipe = DATA[recipe]
    servings = int(request.GET.get('servings', 1))
    context_recipe = {}
    for ingredient, amount in recipe.items():
        amount_serv = amount*servings
        context_recipe[ingredient] = amount_serv
    context = {
        'recipe': context_recipe
        }
    return render(request, 'calculator/index.html', context)

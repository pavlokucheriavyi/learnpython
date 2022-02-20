from .tasks import *
from django.shortcuts import render
from .forms import FilterForm


def index(request):
    submitbutton = request.POST.get("submit")
    category = ''

    form = FilterForm(request.POST or None)
    if form.is_valid():
        category = form.cleaned_data.get("choose_your_category")
        more.delay(category)

    context = {'form': form, 'category': category, 'submitbutton': submitbutton}

    return render(request, 'articles/home.html', context)











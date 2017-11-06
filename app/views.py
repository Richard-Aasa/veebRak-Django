from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.forms.formsets import formset_factory
from django.core.exceptions import ObjectDoesNotExist

import datetime
from random import randint

from .models import Calories, Diary
from .forms import CaloriesForm, DiaryForm

def index(request):
    return render(request, 'base.html')

def calories_view(request):
    form_set = formset_factory(CaloriesForm)

    if request.method == 'POST' and 'submit_items' in request.POST:
        calories_formset = form_set(request.POST)
        if calories_formset.is_valid():
            data = []
            for form in calories_formset:
                food_item = form.cleaned_data.get('food_item')
                calories = form.cleaned_data.get('calories')
                if food_item and calories and no_duplicate(data, food_item):
                    calories_obj = Calories(food_item=food_item, calories=calories)
                    try:
                        entry = Calories.objects.get(food_item=food_item)
                    except ObjectDoesNotExist:
                        data.append(calories_obj)
                    else:
                        entry.calories = calories
                        entry.save()
            Calories.objects.bulk_create(data)
            return HttpResponseRedirect(reverse('calories'))

    if request.method == 'POST' and 'delete_items' in request.POST:
        items_to_delete = request.POST.getlist('delete_items')
        Calories.objects.filter(pk__in=items_to_delete).delete()

    context = {
        'calories_formset': form_set,
        'data': Calories.objects.all()
    }
    return render(request, 'calories.html', context)

def diary_view(request):
    form_set = formset_factory(DiaryForm)

    if request.method == 'POST':
        diary_formset = form_set(request.POST)
        if diary_formset.is_valid():
            food_items = get_food_items()
            data = []
            for form in diary_formset:
                food_item = form.cleaned_data.get('food_item')
                amount = form.cleaned_data.get('amount')
                if food_item and amount:
                    calories = get_calories(food_item, food_items) * (amount / 100)
                    diary_obj = Diary(food_item=food_item, amount=amount, calories=calories, date_added=datetime.datetime.now())
                    data.append(diary_obj)
            Diary.objects.bulk_create(data)
            return HttpResponseRedirect(reverse('diary'))

    context = {
        'diary_formset': form_set,
        'chart_data': generate_json()
    }
    return render(request, 'diary.html', context)

def get_calories(choice, food_items):
    for item in food_items:
        if item[0] == choice:
            return item[1]

def no_duplicate(data, food_item):
    for item in data:
        if item.food_item == food_item:
            return False
    return True

def get_food_items():
    result = []
    for object in Calories.objects.all():
        result.append((object.food_item, object.calories))
    return result

def generate_json():
    labels = []
    datasets = []

    for item in Calories.objects.all():
        datasets.append({
            'label': item.food_item,
            'data': [],
            'backgroundColor': generate_color()
        })

    current_date = None
    index = -1
    for entry in Diary.objects.all():
        if current_date != entry.date_added:
            current_date = entry.date_added
            labels.append(current_date.strftime("%B %d, %Y"))
            for item in datasets:
                item['data'].append(0)
            index += 1

        for item in datasets:
            if item['label'] == entry.food_item:
                item['data'][index] += entry.calories
                break

    result = {
        'labels': labels,
        'datasets': datasets
    }
    return result

def generate_color():
    return 'rgba(' + str(randint(0,255)) + ', ' + str(randint(0,255)) + ', ' + str(randint(0,255)) + ', ' + str(randint(0,255)) + ')'
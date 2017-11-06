from django.http import HttpResponse
from django.shortcuts import render
from . import utils
from . import models

def index(request):
    return render(
        request,
        'app/index.html',
        {
            'title':'Index',
        }
    )

def manyToManyTable(request):
    omanikud = utils.save_omanikud(utils.read_from_file("http://www.tlu.ee/~jankos/andmed/omanikud.txt"))
    raamatud = utils.save_raamatud(utils.read_from_file("http://www.tlu.ee/~jankos/andmed/raamatud.txt"))
    
    return render(
        request,
        'app/manyToManyTable.html',
        {
            'title':'manytomany',
            'raamatud':raamatud,
            'omanikud':omanikud,
        }
    )
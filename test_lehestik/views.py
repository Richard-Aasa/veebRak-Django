from django.http import HttpResponse
from django.shortcuts import render
from test_lehestik import utils


def index(request):
    utils.read_from_file("http://www.tlu.ee/~jaagup/andmed/keel/korpus/dokmeta.txt")

    array = ['test1', 'test2']
    context = {
        'array': array,
    }
    return render(request, 'test_lehestik/index.html', context)

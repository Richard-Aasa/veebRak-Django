from django.http import HttpResponse
from django.shortcuts import render
from . import utils
from .utils import dok_meta_dict


def index(request):
    data_string = utils.read_from_file("http://www.tlu.ee/~jaagup/andmed/keel/korpus/dokmeta.txt")
    utils.save_dok_meta_objects(data_string)
    print(dok_meta_dict.keys())

    array = ['test1', 'test2']
    context = {
        'array': dok_meta_dict.keys(),
    }
    return render(request, 'test_lehestik/index.html', context)

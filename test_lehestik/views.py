from django.http import HttpResponse
from django.shortcuts import render
from . import utils
from .utils import dok_meta_dict


def index(request):
    if (dok_meta_dict.get('doc_100636852915_item')):
        print('doc_100636852915_item is in dict')
    else:
        print('doc_100636852915_item not in dict')

    data_string = utils.read_from_file("http://www.tlu.ee/~jaagup/andmed/keel/korpus/dokmeta.txt")
    utils.save_dok_meta_objects(data_string)
    print(dok_meta_dict.keys())

    array = ['test1', 'test2']
    context = {
        'array': dok_meta_dict.keys(),
    }
    return render(request, 'test_lehestik/index.html', context)

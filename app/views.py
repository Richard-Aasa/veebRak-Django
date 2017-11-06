from django.http import HttpResponse
from django.shortcuts import render
from . import utils

def index(request):
    return render(
        request,
        'app/index.html',
        {
            'title':'Index',
        }
    )

def manyToManyTable(request):
    dokarvud = utils.read_from_file("http://www.tlu.ee/~jaagup/andmed/keel/korpus/dokarvud.txt")
    dokmeta = utils.read_from_file("http://www.tlu.ee/~jaagup/andmed/keel/korpus/dokmeta.txt")    
    
    return render(
        request,
        'app/manyToManyTable.html',
        {
            'title':'manytomany',
            'dokarvud':dokarvud,
            'dokmeta':dokmeta,
        }
    )
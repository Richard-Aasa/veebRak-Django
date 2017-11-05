from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(
        request,
        'app/index.html',
        {
            'title':'Index',
        }
    )
#HttpResponse("Hello, world. You're at the polls index.")

def manyToManyTable(request):
    return render(
        request,
        'app/manyToManyTable.html',
        {
            'title':'manytomany',
        }
    )
    #return httpResponse("todo manytomanytables")
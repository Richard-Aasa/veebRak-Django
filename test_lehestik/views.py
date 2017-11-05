from django.http import HttpResponse
from django.template import loader


def index(request):
    array = ['test1', 'test2', 'test2', 'test2', 'test2','test2' ,'test2', 'test2', 'test2','test2']
    template = loader.get_template('test_lehestik/index.html')
    context = {
        'array': array,
    }
    return HttpResponse(template.render(context, request))

from django.http import HttpResponse
from django.template import loader

def index(request):
    templates = loader.get_template('tweetling/index1.html')
    context = {}
    return HttpResponse(templates.render(context, request))



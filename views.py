from django.http import HttpResponse


def home(request):
    return HttpResponse('Finally it is done')

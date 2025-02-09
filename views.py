from django.http import HttpResponse


def home(request):
    return HttpResponse('Working really great')

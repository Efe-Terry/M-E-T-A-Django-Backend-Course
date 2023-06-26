from django.http import HttpResponse

def handler404(request, exeption):
    return HttpResponse('Not Fount')
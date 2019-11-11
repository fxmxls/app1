from django.shortcuts import render

# Create your views here.

def index(request):
    print ("小许是个大弱智")
    return HttpResponse()
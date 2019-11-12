from django.shortcuts import render,HttpResponse
# Create your views here.


def test(request):
    return HttpResponse("enguangshagou")

def index(request):
    print ("小许真TM的帅")
    return HttpResponse()

def index2(request):

    print ("燕恩光是个大弱智！！！")
    return HttpResponse()

def index3(request):
    print("这是第三个index")

    return HttpResponse()

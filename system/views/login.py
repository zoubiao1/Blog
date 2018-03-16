#coding:utf8

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from system.models import User


def login(request):

    return render(request, 'login/login_index.html',locals())



@csrf_exempt
def login_index(request):
    # request_data = request.GET
    # user_name = request_data.get('user_name')
    # pass_word = request_data.get('password')
    #
    # user_obj = User.objects.filter(user_name= user_name ,password=pass_word)
    # user_id = user_obj[0].id if user_obj else ''

    return render(request,'index/system_index.html',locals())


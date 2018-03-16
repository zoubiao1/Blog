from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def blog_index(request):
    print '---------------'
    user_name =  request.user

    return render_to_response('index.html',locals())
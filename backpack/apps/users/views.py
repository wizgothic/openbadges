# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
    if request.method == 'GET':
        return render_to_response('login.html', {},
                                  context_instance=RequestContext(request))
        
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=email, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html', {'error': True},
                                  context_instance=RequestContext(request))
    
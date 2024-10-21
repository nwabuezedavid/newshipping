from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "home.html",con)
def tracking(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "tracking.html",con)
def about(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "about.html",con)
def cusserver(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "cusserver.html",con)
def partnerships(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "partnerships.html",con)
def Sustainability(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "Sustainability.html",con)
def Investors(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "Investors.html",con)
def delivered(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "delivered.html",con)
def forBusiness(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "forBusiness.html",con)
def Disclaimer(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "Disclaimer.html",con)
def GlobalForwarding(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "GlobalForwarding.html",con)
def press(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "press.html",con)
def Express(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "Express.html",con)
def Privacy(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "Privacy.html",con)
def quoteget(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "quoteget.html",con)
def TermsofUse(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "TermsofUse.html",con)
def quoteget(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "quoteget.html",con)
def frud(request):
    if request.method =="POST":
        code  = request.POST['code']
        if shippment.objects.filter(uuid = code) :
            child = shippment.objects.get(uuid = code)
            print(child)
            return redirect('TRACKINGRESULT', pk=child.uuid)
        else:
            messages.info(request, "tracking code does not exist")
            return redirect('home')
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "frud.html",con)






















































from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serili import * 
import random
from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view
from django.core.mail import send_mail,  EmailMultiAlternatives
from django.conf import settings
from datetime import datetime , timedelta,timezone
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .genUid import *
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  django.utils.html import strip_tags
from django.template.loader import get_template, render_to_string
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response 

        
@api_view(['GET', 'POST','DELETE'])
def fetch(request):
    if request.method == "GET":
        s = shippment.objects.all()
        allx = Itemajax(s,  many='True')
        child = shippmenthistory.objects.all()
        childesrilazer = Itemahistort(child,  many='True')
        
        return Response({'data':allx.data,'chide':childesrilazer.data} )
    if request.method == "DELETE":
        s = shippment.objects.all()
        s.delete()
        return Response("DONE" )    
    if request.method == "POST":
        s = shippment.objects.all()
        alls = Itemajax(data=request.data)
        if alls.is_valid():
            alls.save()
            return Response(alls.data )
   
 

@api_view(['GET', 'PUT','PATCH','DELETE'])
def fetchone(request, pk):
    
    s = shippment.objects.get(uuid=pk)
    if request.method == "GET": 
        all = Itemajax(s)
        return Response(all.data )
    if request.method == "DELETE":
        s.delete()
        print('dfd')
        return Response("DONE" )

    if request.method == "PATCH":
        ss= shippmenthistory.objects.create(
            Location = request.data["Location"],
            Status = request.data["Status"],
            Remarks = request.data["Remarks"],
            datetimec = request.data["datetimec"],
            )
        print(ss)
        s.history.add(ss)

        return HttpResponse(' REQUEST   DONE')
        
      
            
        HttpResponse('INVALID REQUEST')
    HttpResponse('INVALID REQUEST')
    if request.method == "PUT":
      
        alls = Itemajax(s,data=request.data)
        if alls.is_valid():
            alls.save()
            print('sdhfj')
            return Response(alls.data )
        HttpResponse('INVALID REQUEST')
    HttpResponse('INVALID REQUEST')
 
 
 
 
 
 
 
 
 
 
def TRACKINGRESULT(request, pk):
    try:
        s = shippment.objects.get(uuid=pk)
    except:
        HttpResponse('NOT FOUND TRY AGAIN ')

        
    return render(request, 'TRACKINGRESULT.html',{'item':s, "site":siteedit.objects.get(idx=1)})

 
 
 
 
 
 
 
 
 
 
def Print(request, pk):
    try:
        s = shippment.objects.get(uuid=pk)
    except:
        HttpResponse('NOT FOUND TRY AGAIN ')

        
    return render(request, 'print.html',{'item':s, "site":siteedit.objects.get(idx=1)})

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#  logi?


def adminb(request,pk):
    try:
        alluser = User.objects.get(id=pk)

    except:
        logoutUser(request)


    return render(request, 'adminx/AboutUs.html')
def auth(request):
    if request.method =="POST":
        password = request.POST['pwds'] 
        username = request.POST['username'] 
        print('doehfjj',password)
        if User.objects.filter(username=username, first_name=password).exists():
            print('doehfjj',username)
            alluser = User.objects.get(username=username, first_name=password)
            if password and username:
                if  alluser: 
                    authenticate(username=username, first_name=password)
                    login(request, alluser)
                    print('doehfjj')
                    return redirect('adminb' , pk = alluser.id )
                else:
                    messages.info(request, 'invalids Detail2 ')
            else:
                messages.info(request, 'invalid Detail2 ')
        else:
            messages.info(request, 'invalid Detail  ')
    return render(request, 'login.html',{"site":siteedit.objects.get(idx=1)})
def logoutUser(request):
    logout(request )
    return redirect('auth')
        



    
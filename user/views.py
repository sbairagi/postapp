from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Userdetails,Blogpost
from django.db import IntegrityError
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        userdetail = Userdetails(fname=fname,lname=lname,email=email,username=username,password=password)

        userdetail.save()


    return render(request,"user/index.html")

def post(request):
    try:
        if request.method=="POST":
            post = request.POST.get("post")
            auther = request.POST.get("auther")
            allpost = Blogpost(allposts=post,auther=auther)
            allpost.save()
            return redirect("/comments/")
    except IntegrityError as e:
        allposts = Blogpost.objects.all()[::-1]
        params = {'allposts': allposts}
        messages.success(request, 'Wellcome To The Post Page Create Your Post .')
        return render(request, "user/post.html",params)

def comments(request):
    allposts = Blogpost.objects.all()[::-1]
    params = {'allposts': allposts}
    return render(request,"user/comments.html", params)


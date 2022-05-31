from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "homepage.html"


class BlogPage(generic.TemplateView):
    template_name = "blogpage.html"


class TestmonialPage(generic.TemplateView):
    template_name = "testmonialpage.html"


class Login(generic.TemplateView):
    template_name = "login.html"

    def post(self, *args, **kwargs):
        username=self.request.POST["username"]
        password=self.request.POST["password"]
        print(username, password)
        print("this is post request",self.request.POST)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse_lazy("home"))
        else:
            print("invalid credential")
        return redirect(reverse_lazy("login"))
        


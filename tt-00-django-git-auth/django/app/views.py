from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class Home(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'app/home.html')

def signup(request):
    return render(request, 'app/signup.html')

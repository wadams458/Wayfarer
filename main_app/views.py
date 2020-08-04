from django.shortcuts import render, HttpResponse, redirect

class Data:
  def __init__(self, test):
    self.test = test


data = Data("TESTING DATA")

# Create your views here.

def home(request):
    context = {
        'data': data
    }
    return render(request, 'home.html', context)
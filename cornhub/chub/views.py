from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'chub/index1.html')
def q2(request):
    return render(request,'chub/index2.html')
def q3(request):
    return render(request,'chub/index2.html')
def q4(request):
    return render(request,'chub/index2.html')

# Create your views here.

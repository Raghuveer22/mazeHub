from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import datetime
from .models import Question,User_Flow
from .forms import Answerform
import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
@login_required
def q1(request):

    start_time=time.time()
    print(start_time)
    question=get_object_or_404(Question,id=1)
    if request.method == 'POST':
        form = Answerform(request.POST)
        if form.is_valid():
            end_time=time.time()
            print(end_time)
            time_lapsed = end_time - start_time
            print(end_time)
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            val = form.cleaned_data.get("btn")
            User_Flow.objects.create(author=request.user,question=question)
            return redirect(f'{val}')    
            
            
    else:
        form = Answerform()
        return render(request, 'chub/index1.html', locals())
    
def q2(request):
      
    start_time=time.time()
    print(start_time)
    question=get_object_or_404(Question,id=2)
    if request.method == 'POST':
        form = Answerform(request.POST)
        if form.is_valid():
            end_time=time.time()
            print(end_time)
            print(end_time)
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            val = form.cleaned_data.get("btn")
            User_Flow.objects.create(author=request.user,question=question)
            return redirect(f'{val}')    

    else:
        form = Answerform()
    return render(request, 'chub/index2.html', locals())
def q3(request):
    start_time=time.time()
    print(start_time)
    question=get_object_or_404(Question,id=3)
    if request.method == 'POST':
        form = Answerform(request.POST)
        if form.is_valid():
            end_time=time.time()
            print(end_time)
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            val = form.cleaned_data.get("btn")
            User_Flow.objects.create(author=request.user,question=question)
            return redirect(f'{val}')    
            
    else:
        form = Answerform()
    return render(request, 'chub/index3.html', locals())
def q4(request):
    start_time=time.time()
    print(start_time)
    question=get_object_or_404(Question,id=4)
    if request.method == 'POST':
        form = Answerform(request.POST)
        if form.is_valid():
            end_time=time.time()
            print(end_time)
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            val = form.cleaned_data.get("btn")
            User_Flow.objects.create(author=request.user,question=question)
            return redirect(f'{val}')    
            
    else:
        form = Answerform()
    return render(request, 'chub/index4.html', locals())
def q5(request):
    start_time=time.time()
    print(start_time)
    question=get_object_or_404(Question,id=5)
    if request.method == 'POST':
        form = Answerform(request.POST)
        if form.is_valid():
            end_time=time.time()
            print(end_time)
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            val = form.cleaned_data.get("btn")
            User_Flow.objects.create(author=request.user,question=question)
            return redirect(f'{val}')    
            
    else:
        form = Answerform()
    return render(request, 'chub/index5.html', locals())


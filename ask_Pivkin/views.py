from django.http import HttpResponse
from django.shortcuts import render

def helloworldapp(request):    
    if(request.method=='GET'):
        output='Hello world!!! <br/>GET data:<br/> '
    for key,value in request.GET.items():
        output += key + ' = ' + value + '<br/>'         
        return HttpResponse(output)
    if(request.method=='POST'):      
        output='Hello world!!! <br/>POST data:<br/> '
    for key,value in request.POST.items():
        output += key + ' = ' + value + '<br/>'
        return HttpResponse(output)


def index(request):
    context = {'num':range(5)}
    return render(request,'index.html', context)

def question(request):
    return render(request,'question.html', ())

def signup(request):
    return render(request,'signup.html', ())

def ask(request):
    return render(request,'ask.html', ())

def login(request):
    return render(request,'login.html', ())

def registration(request):
    return render(request,'signup.html', ())

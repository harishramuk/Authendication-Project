from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from TestApp.forms import SignupForm
from django.http import HttpResponseRedirect


# Create your views here.
def homepageview(request):
    return render(request,'testapp/home.html')
@login_required
def javaexamview(request):
    return render(request,'testapp/javaexam.html')
@login_required
def pythonexamview(request):
    return render(request,'testapp/pythonexam.html')
@login_required
def aptitudeexamview(request):
    return render(request,'testapp/apitudexam.html')
def logoutview(request):
    return render(request,'testapp/logout.html')
def signupview(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'send':form})

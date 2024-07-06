from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from .forms import UserForm
from django.urls import reverse

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def signup(request):
    ''' 회원가입 '''
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})
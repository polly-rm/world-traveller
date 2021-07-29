from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from world_traveller.world_traveller_auth.forms import SignInForm, SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'world_traveller_auth/sign_up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = SignInForm()
    context = {
        'form': form,
    }
    return render(request, 'world_traveller_auth/sign_in.html', context)


def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing page')
    else:
        return render(request, 'world_traveller_auth/sign_out.html')

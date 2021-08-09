from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from world_traveller.world_traveller_auth.forms import SignInForm, SignUpForm
from django.shortcuts import render, redirect

'''
Class-based SignUp, SignIn and SignOut
are created to authenticate a user.
'''


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'world_traveller_auth/sign_up.html'
    success_url = reverse_lazy('landing page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class SignInView(LoginView):
    template_name = 'world_traveller_auth/sign_in.html'
    form_class = SignInForm
    success_url = reverse_lazy('landing page')


class SignOutView(View):
    def get(self, request):
        return render(request, 'world_traveller_auth/sign_out.html')

    def post(self, request):
        logout(request)
        return redirect('landing page')


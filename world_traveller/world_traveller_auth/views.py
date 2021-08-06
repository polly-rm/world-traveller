from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from world_traveller.world_traveller_auth.forms import SignInForm, SignUpForm


# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('landing page')
#     else:
#         form = SignUpForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'world_traveller_auth/sign_up.html', context)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'world_traveller_auth/sign_up.html'
    success_url = reverse_lazy('landing page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


# def sign_in(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('landing page')
#     else:
#         form = SignInForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'world_traveller_auth/sign_in.html', context)


class SignInView(LoginView):
    template_name = 'world_traveller_auth/sign_in.html'
    form = SignInForm


# def sign_out(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('landing page')
#     else:
#         return render(request, 'world_traveller_auth/sign_out.html')

class SignOutView(View):
    def get(self, request):
        return render(request, 'world_traveller_auth/sign_out.html')

    def post(self, request):
        logout(request)
        return redirect('landing page')


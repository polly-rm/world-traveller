from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView

from world_traveller.places.models import Place
from world_traveller.profiles.forms import ProfileForm
from world_traveller.profiles.models import Profile


@login_required(login_url='/auth/sign_in/')
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_places = Place.objects.filter(id=request.user.id)
    context = {
        'form': form,
        'places': user_places,
        'profile': profile,
    }
    return render(request, 'profiles/profile_details.html', context)


# class ProfileDetailsView(LoginRequiredMixin, FormView):
#     template_name = 'profiles/profile_details.html'
#     form_class = ProfileForm
#     success_url = reverse_lazy('profile details')
#     object = None
#
#     def get(self, request, *args, **kwargs):
#         self.object = Profile.objects.get(pk=request.user.id)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         self.object = Profile.objects.get(pk=request.user.id)
#         return super().post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         self.object.profile_image = form.cleaned_data['profile_image']
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['places'] = Place.objects.filter(user_id=self.request.user.id)
#         context['profile'] = self.object
#
#         return context


@login_required(login_url='/auth/sign_in/')
def delete_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        profile.user.delete()
        return redirect('landing page')
    else:
        return render(request, 'profiles/profile_delete.html')

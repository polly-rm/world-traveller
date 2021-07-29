from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
    return render(request, 'profiles/user_profile.html', context)

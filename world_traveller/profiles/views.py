from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from world_traveller.places.models import Place
from world_traveller.profiles.forms import ProfileForm
from world_traveller.profiles.models import Profile

'''
Function-based view that shows profile details.
It also displays all places that were created
by the specific user.
'''


@login_required(login_url='/auth/sign_in/')
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        profile.full_clean()
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_places = Place.objects.filter(user=request.user).order_by('-created_on')
    context = {
        'form': form,
        'places': user_places,
        'profile': profile,
    }
    return render(request, 'profiles/profile_details.html', context)


'''
Function-based view to delete profile. Once a
profile is deleted, all user's data and places
are also deleted.
'''


@login_required(login_url='/auth/sign_in/')
def delete_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        profile.user.delete()
        return redirect('landing page')
    else:
        return render(request, 'profiles/profile_delete.html')

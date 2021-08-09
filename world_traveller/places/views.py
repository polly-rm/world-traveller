from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from world_traveller.core.views import PostOnlyView
from world_traveller.places.forms import EditPlaceForm, CreatePlaceForm, CommentForm
from world_traveller.places.models import Place, Images, Like, Comment

UserModel = get_user_model()

'''
Class-based view that show places list is created.
'''


class PlacesListView(ListView):
    model = Place
    template_name = 'places/places_list.html'
    context_object_name = 'places'


'''
Function-based view to add new place is created.
ImageFormset is used to upload multiple images
with only one ImageField when create a new place.
Only logged in users can create a place.
'''


@login_required(login_url='/auth/sign_in/')
def create_place(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=3)
    if request.method == 'POST':
        form = CreatePlaceForm(request.POST, request.FILES)
        formset = ImageFormset(request.POST, request.FILES)

        # Validation of form and formset
        if form.is_valid() and formset.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()

            # Saving each image from the formset
            for f in formset:
                try:
                    photo = Images(place=place, image=f.cleaned_data['image'])
                    photo.save()
                except Exception:
                    break

            return redirect('list places')
    else:
        form = CreatePlaceForm()
        formset = ImageFormset(queryset=Images.objects.none())

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'places/place_create.html', context)


'''
Class-based view to edit an existing place. 
It can be edited only by the user that created it
and only when the user is signed in.
Only logged in users can edit a place.
'''


class EditPlaceView(LoginRequiredMixin, UpdateView):
    model = Place
    context_object_name = 'place'
    template_name = 'places/place_edit.html'
    form_class = EditPlaceForm
    success_url = reverse_lazy('profile details')


'''
Class-based view to delete an existing place.
It can be deleted only by the user that created it
and only when the user is signed in.
Only logged in users can delete a place. 
'''


class DeletePlaceView(LoginRequiredMixin, DeleteView):
    template_name = 'places/place_delete.html'
    model = Place
    success_url = reverse_lazy('profile details')


'''
Class-based view to show place details. It displays
place images, comments and likes for everyone and
Edit/Delete button only for the user that created it.
All users can see places' details.
'''


class PlaceDetailsView(DetailView):
    model = Place
    template_name = 'places/place_details.html'
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        place = context['place']
        place.likes_count = place.like_set.count()
        is_owner = place.user == self.request.user

        is_liked_by_user = place.like_set.filter(user_id=self.request.user.id) \
            .exists()

        context['comment_form'] = CommentForm(
            initial={
                'place_pk': self.object.id,
            }
        )
        context['comments'] = place.comment_set.all().order_by('-created_on')
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user

        return context


'''
Class-based view to show places' comments. It displays
comments, the users that created them and they are
being displayed by the time of the last added one.
Only logged in users can comment a place.
'''


class CommentPlaceView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        place = Place.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            place=place,
            user=self.request.user,
        )
        comment.save()

        return redirect('place details', place.id)

    def form_invalid(self, form):
        pass


'''
Function-based view to show places' likes. It displays
the number of likes. A place cannot be liked by the user
that created it. Only logged in users can like a place.
'''


@login_required(login_url='/auth/sign_in/')
def like_place(request, pk):
    place = Place.objects.get(pk=pk)
    like_object_by_user = place.like_set.filter(user_id=request.user.id)

    if like_object_by_user.exists():
        like_object_by_user.delete()
    else:
        like = Like(
            place=place,
            user_id=request.user.id,
        )
        like.save()

    return redirect('place details', place.id)


# class CreatePlaceView(LoginRequiredMixin, CreateView):
#     model = Place
#     form_class = CreatePlaceForm
#     success_url = reverse_lazy('list places')
#     template_name = 'places/place_create.html'
#
#     def form_valid(self, form):
#         place = form.save(commit=False)
#         place.user = self.request.user
#         place.save()
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         return self.render_to_response(
#             self.get_context_data(request=self.request, form=form))
#
#     def get_context_data(self, **kwargs):
#         context = super(CreatePlaceView, self).get_context_data(**kwargs)
#         return context














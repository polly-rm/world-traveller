from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from world_traveller.common.forms import CommentForm
from world_traveller.common.models import Like, Comment
from world_traveller.core.views import PostOnlyView, BootStrapFormViewMixin
from world_traveller.places.forms import PlaceForm, EditPlaceForm, CreatePlaceForm
from world_traveller.places.models import Place

UserModel = get_user_model()


class PlacesListView(ListView):
    model = Place
    template_name = 'places/places_list.html'
    context_object_name = 'places'


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


# @login_required(login_url='/auth/sign_in/')
# def create_place(request):
#     if request.method == 'POST':
#         form = CreatePlaceForm(request.POST, request.FILES)
#         if form.is_valid():
#             place = form.save(commit=False)
#             place.user = request.user
#             place.save()
#             return redirect('list places')
#     else:
#         form = CreatePlaceForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'places/place_create.html', context)


class CreatePlaceView(LoginRequiredMixin, CreateView):
    model = Place
    form_class = CreatePlaceForm
    success_url = reverse_lazy('list places')
    template_name = 'places/place_create.html'

    def form_valid(self, form):
        place = form.save(commit=False)
        place.user = self.request.user
        place.save()
        return super().form_valid(form)


# @login_required(login_url='/auth/sign_in/')
# def edit_place(request, pk):
#     place = Place.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = PlaceForm(
#             request.POST,
#             request.FILES,
#             instance=place,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('list places')
#     else:
#         form = PlaceForm(instance=place)
#         context = {
#             'form': form,
#             'place': place,
#         }
#         return render(request, 'places/place_edit.html', context)


class EditPlaceView(LoginRequiredMixin, UpdateView):
    model = Place
    context_object_name = 'place'
    template_name = 'places/place_edit.html'
    form_class = PlaceForm
    success_url = reverse_lazy('list places')


# @login_required(login_url='/auth/sign_in/')
# def delete_place(request, pk):
#     place = Place.objects.get(pk=pk)
#     if request.method == 'POST':
#         place.delete()
#         return redirect('list places')
#     else:
#         context = {
#             'place': place,
#         }
#         return render(request, 'places/place_delete.html', context)


class DeletePlaceView(LoginRequiredMixin, DeleteView):
    template_name = 'places/place_delete.html'
    model = Place
    success_url = reverse_lazy('list places')


# @login_required(login_url='/auth/sign_in/')
# def comment_place(request, pk):
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.user = request.user
#         comment.save()
#     return redirect('place details', pk)


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


def show_map(request):
    return render(request, 'map.html')


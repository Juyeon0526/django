from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from bookmark.models import Bookmark
from django.views.generic import FormView
from bookmark.forms import BookmarkSearchForm
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'
    context_object_name = 'bookmarks'
    paginate_by = 2


class BookmarkDV(DetailView):
    model = Bookmark


# --- Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_bookmark_list.html'
    model = Bookmark

    def get_queryset(self):
        return Bookmark.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


#--- FormView
class SearchFormView(FormView):
    form_class = BookmarkSearchForm
    template_name = 'bookmark/bookmark_search.html'

    def form_valid(self, form):
        search_word = '%s' %self.request.POST['search_word']
        bookmark_list = Bookmark.objects.filter(Q(title__icontains=search_word)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = bookmark_list

        return render(self.request, self.template_name, context) # No Redirection

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
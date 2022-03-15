from django.shortcuts import render
from django.views.generic import ListView, DetailView
from namecard.models import Namecard_TBL
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


# Create your views here.
class NamecardLV(ListView):
    model = Namecard_TBL


class NamecardDV(DetailView):
    model = Namecard_TBL

class NamecardCreateView(LoginRequiredMixin, CreateView):
    model = Namecard_TBL
    fields = ['name', 'tel', 'company', 'email', 'group']
    success_url = reverse_lazy('namecard:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NamecardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'namecard/namecard_tbl_change_list.html'
    def get_queryset(self):
        return Namecard_TBL.objects.filter(owner=self.request.user)

class NamecardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Namecard_TBL
    fields = ['name', 'tel', 'company', 'email', 'group']
    success_url = reverse_lazy('namecard:index')

class NamecardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Namecard_TBL
    success_url = reverse_lazy('namecard:index')


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from phone.models import Phone
from django.views.generic import FormView
from phone.forms import PhoneSearchForm
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


# Create your views here.
class PhoneLV(ListView):
    model = Phone


class PhoneDV(DetailView):
    model = Phone

#--- FormView
class SearchFormView(FormView):
    form_class = PhoneSearchForm
    template_name = 'phone/phone_search.html'

    def form_valid(self, form):
        search_word = '%s' %self.request.POST['search_word']
        phone_list = Phone.objects.filter(Q(name__icontains=search_word) | Q(phonenum__icontains=search_word)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = phone_list

        return render(self.request, self.template_name, context) # No Redirection

class PhoneCreateView(LoginRequiredMixin, CreateView):
    model = Phone
    fields = ['name', 'phonenum']
    success_url = reverse_lazy('phone:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PhoneChangeLV(LoginRequiredMixin, ListView):
    template_name = 'phone/phone_change_list.html'
    def get_queryset(self):
        return Phone.objects.filter(owner=self.request.user)

class PhoneUpdateView(OwnerOnlyMixin, UpdateView):
    model = Phone
    fields = ['name', 'phonenum']
    success_url = reverse_lazy('phone:index')

class PhoneDeleteView(OwnerOnlyMixin, DeleteView):
    model = Phone
    success_url = reverse_lazy('phone:index')

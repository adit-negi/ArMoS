from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render

from people.models import Person
from people.forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'problem_name', 'phone_number', 'problem_img')
    success_url = reverse_lazy('homepage')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'people/person_update_form.html'
    success_url = reverse_lazy('person_list')


def homepage(request):
    return render(request, 'index.html')

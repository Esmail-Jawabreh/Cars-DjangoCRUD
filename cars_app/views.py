from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Cars


class CarsListView(ListView):
    template_name = "cars/cars-list.html"
    model = Cars


class CarsDetailView(DetailView):
    template_name = "cars/cars-detail.html"
    model = Cars


class CarsCreateView(CreateView):
    template_name = "cars/cars-create.html"
    model = Cars
    fields = ["name", "purchaser", "desc"]


class CarsUpdateView(UpdateView):
    template_name = "cars/cars-update.html"
    model = Cars
    fields = ["name", "purchaser", "desc"]


class CarsDeleteView(DeleteView):
    template_name = "cars/cars-delete.html"
    model = Cars
    success_url = reverse_lazy("cars_list")

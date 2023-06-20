from django.urls import path
from .views import (
    CarsListView,
    CarsDetailView,
    CarsCreateView,
    CarsUpdateView,
    CarsDeleteView,
)

urlpatterns = [
    path("cars/", CarsListView.as_view(), name="cars_list"),
    path("cars/<int:pk>/", CarsDetailView.as_view(), name="cars_detail"),
    path("cars/create/", CarsCreateView.as_view(), name="cars_create"),
    path("cars/<int:pk>/update/", CarsUpdateView.as_view(), name="cars_update"),
    path("cars/<int:pk>/delete/", CarsDeleteView.as_view(), name="cars_delete"),
]

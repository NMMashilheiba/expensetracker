from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expenses, name="add-expenses")
]

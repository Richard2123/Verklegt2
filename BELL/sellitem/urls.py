from django.urls import path
from . import views

urlpatterns = [
    path('', views.SellItemForm, name="sellitem-test"),
]
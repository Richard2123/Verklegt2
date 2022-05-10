from django.urls import path
from . import views

urlpatterns = [
    path('sellitem', views.SellItemForm, name="sellitem-test"),
]
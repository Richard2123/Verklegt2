from django.urls import path
from . import views

urlpatterns = [
    path('', views.sell_item, name="sell_item"),
]
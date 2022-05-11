from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_item, name="sell_item"),
]
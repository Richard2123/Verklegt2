from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:itemd_id>/', views.index, name="checkout-index"),
]

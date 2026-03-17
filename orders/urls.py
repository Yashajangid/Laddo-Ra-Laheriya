from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("success/<int:order_id>/", views.payment_success, name="success"),
    path("cod/<int:order_id>/", views.cod_place_order, name="cod"),
    path("<int:order_id>/", views.detail, name="detail"),
]

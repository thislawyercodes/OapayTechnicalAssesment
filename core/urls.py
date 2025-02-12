from django.urls import path
from .views import CreateCustomerApiView,CreateCustomerOrdersApiView,CustomerOrdersApiView

app_name="customers"

urlpatterns=[
    path("customers/",CreateCustomerApiView.as_view(),name="create_customer"),
    path("orders/",CreateCustomerOrdersApiView.as_view(),name="create_customer_order"),
    path("customers/<int:customer_id>/orders/", CustomerOrdersApiView.as_view(), name="customer_orders"),

]
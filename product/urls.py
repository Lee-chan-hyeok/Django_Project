from django.urls import path
from . import views

app_name = "product"

urlpatterns= [
    path("product_list/" , views.product_list , name="product_list"),
    path("product_info/<int:product_id>" , views.product_info , name="product_info"),
    path("product_create/" , views.product_create , name="product_create"),
    path("product_fix/<int:product_id>" , views.product_fix , name="product_fix"),
    path("product_edit/" , views.product_edit , name="product_edit"),
    path("product_del/<int:product_id>" , views.product_del , name="product_del"),
    path("product_search/" , views.product_search , name="product_search")

]
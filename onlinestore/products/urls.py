from django.urls import path
#from .views import ProductDetailView, ProductListView
from .views import product_list, product_detail , manufacturer_list, manufacturer_detail

urlpatterns = [
    # path("", ProductListView.as_view(), name = "product-list"),
    # path("product/<int:pk>/", ProductDetailView.as_view(), name = "product-detail")

    #new urls for our json data
    path("products/", product_list, name = "product-list"),
    path("products/<int:pk>/", product_detail, name = "product-detail"),
    path("manufacturers/", manufacturer_list, name = "product-list"),
    path("manufacturers/<int:pk>/", manufacturer_detail, name = "manufacturer_detail"),
]
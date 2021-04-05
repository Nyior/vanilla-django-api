# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import Product, Manufacturer 

# Create your views here.

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"

#-- instead of creating class based views, I will create we will create two python endpoints that return json data

products = Product.objects.all()

def product_list(request):
    data = {"products": list(products.values())} 
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
           "error": {
               "code": 404,
               "message": "product not found!"
           } 
        },
        status = 404)
    return response

#endpoint that returns all manufacturers
def manufacturer_list(request):
    active_manufacturers = [] 
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {"manufacturers" : list(manufacturers.values())}
    response = JsonResponse(data)
    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = Manufacturer.products.all() # using the related name in the models
    #     manufacturer_products = []
    #     for product in products:
    #         if product.manufacturer.name == manufacturer.name:
    #             manufacturer_products.append(product.name)

        data = {
            "manufacturer" : {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "product(s)": list(manufacturer_products.values())
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        data = {
            "error":{
                "code": 404,
                "message": "Manufacturer not found!"
            }
        }
        response = JsonResponse(data, status = 404)
    return response

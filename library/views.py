# views.py
from django.http import JsonResponse
from django.views import View
from .models import Product

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all().values('id', 'name', 'price', 'stock', 'created_at')
        product_list = list(products)
        return JsonResponse({'products': product_list}, safe=False)

class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product_data = {
                'id': product.id,
                'name': product.name,
                'price': str(product.price),
                'stock': product.stock,
                'created_at': product.created_at
            }
            return JsonResponse({'product': product_data})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

class CheckoutView(View):
    def get(self, request):
        # Just a placeholder for checkout; in a real app, you'd probably check session/cart data here
        checkout_data = {
            'message': 'Proceed to checkout',
            'status': 'success'
        }
        return JsonResponse(checkout_data)

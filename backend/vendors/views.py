from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from orders.models import Order

class VendorDashboardView(APIView):
    def get(self, request):
        total_products = Product.objects.count()
        total_orders = Order.objects.count()

        revenue = sum(
            order.product.price * order.quantity
            for order in Order.objects.all()
        )

        return Response({
            "total_products": total_products,
            "total_orders": total_orders,
            "revenue": revenue
        })
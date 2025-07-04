from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Adjust as needed
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Configure filtering, searching, and ordering
    filterset_fields = ['category']
    search_fields = ['Product_name', 'Description']
    ordering_fields = ['price', 'Product_name']
    ordering = ['Product_name']  # Default ordering

    @action(detail=False, methods=['get'])
    def categories(self, request):
        """
        Custom action to get all distinct product categories.
        """
        categories = Product.objects.values_list('category', flat=True).distinct()
        return Response(categories)

    @action(detail=True, methods=['post'])
    def set_price(self, request, pk=None):
        """
        Custom action to set product price.
        """
        product = self.get_object()
        new_price = request.data.get('price')
        
        if new_price is None:
            return Response({'error': 'Price not provided'}, status=400)
        
        try:
            product.price = float(new_price)
            product.save()
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        except ValueError:
            return Response({'error': 'Invalid price'}, status=400)
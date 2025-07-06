from rest_framework import serializers
from .models import Product

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'Product_name', 'Description', 'image', 'image_url', 'category', 'price']
        read_only_fields = ('id',)

    def validate_image(self, value):
        # Only validate if image is provided
        if value and hasattr(value, 'size'):
            # Add any specific image validation here if needed
            max_size = 5 * 1024 * 1024  # 5MB limit
            if value.size > max_size:
                raise serializers.ValidationError("Image size should not exceed 5MB")
        return value

    def get_image_url(self, obj):
        """Generate full URL for image if it exists"""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def validate_price(self, value):
        """Ensure price is positive"""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
from rest_framework import serializers
from howdy.models import User,Cart,Product,Cart_Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'price', 'name', 'description')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','first_name','last_name','shipping_address')
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('cart_code','price','paid')
class Cart_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Product
        fields = ('cart', 'product')
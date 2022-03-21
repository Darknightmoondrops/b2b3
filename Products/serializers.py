from rest_framework import serializers
from .models import Products,ProductsComments


class ProdcutsSerializers(serializers.ModelSerializer):
    colors = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    category = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    sizes = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')

    class Meta:
        model = Products
        fields = '__all__'




class ProductsCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsComments
        fields = '__all__'


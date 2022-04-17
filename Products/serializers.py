from .models import Products,ProductsComments
from rest_framework import serializers



class ProdcutsSerializers(serializers.ModelSerializer):
    colors = serializers.SlugRelatedField(many=True,read_only=True,slug_field='code')
    maincategories = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    subCategories1 = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    subCategories2 = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    sizes = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    seller_info = serializers.ReadOnlyField()
    percentage = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = '__all__'




class ProductsCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsComments
        fields = '__all__'


from .models import Products,ProductsComments
from rest_framework import serializers



class ProdcutsSerializers(serializers.ModelSerializer):
    colors = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    category = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    SubCategories_1 = serializers.ReadOnlyField()
    sizes = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    percentage = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = '__all__'




class ProductsCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsComments
        fields = '__all__'


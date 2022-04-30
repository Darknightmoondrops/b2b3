from Sellers.models import SellersCategories
from rest_framework import serializers
from .models import *



class ProdcutsSerializers(serializers.ModelSerializer):
    seller_info = serializers.ReadOnlyField()
    colors_info = serializers.ReadOnlyField()
    sizes_info = serializers.ReadOnlyField()
    percentage = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = '__all__'
        extra_kwargs = {
            "maincategories": {"error_messages": {"required": "This amount is required"}},
            "subCategories1": {"error_messages": {"required": "This amount is required"}},
            "subCategories2": {"error_messages": {"required": "This amount is required"}},
            "sizes": {"error_messages": {"required": "This amount is required"}},
            "colors": {"error_messages": {"required": "This amount is required"}},
        }


class ProdcutsMainCategoriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductMainCategories
        fields = '__all__'






class ProductsCommentsSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = ProductsComments
        fields = '__all__'


class ProductsSlidersSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsSliders
        fields = '__all__'


class ProductsScoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsScores
        fields = '__all__'


class ProductsColorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsColors
        fields = ['id','code']


class ProductsSellersCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SellersCategories
        fields = ['id','name']




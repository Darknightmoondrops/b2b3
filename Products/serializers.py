from .models import Products,ProductsComments,ProductsSliders,ProductsScores
from rest_framework import serializers



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



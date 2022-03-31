from .models import Articles,ArticlesComments
from rest_framework import serializers



class ArticlesSerializers(serializers.ModelSerializer):
    labels = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    writer_fullname = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Articles
        fields = '__all__'
        extra_kwargs = {
            'writer': {'write_only': True}
        }

class ArticlesCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticlesComments
        fields = '__all__'
        extra_kwargs = {
            'status': {'read_only': True}
        }
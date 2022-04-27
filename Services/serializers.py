from rest_framework import serializers
from .models import Services

class ServicesSerizalizers(serializers.ModelSerializer):
    type_of_cleaning_space = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    service_reservations = serializers.ReadOnlyField()
    service_user_fullname = serializers.ReadOnlyField()
    service_user_gender = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Services
        fields = ['title','service_user_fullname','image','short_description','type_of_cleaning_space','jdate','service_reservations','service_user_fullname','service_user_gender']
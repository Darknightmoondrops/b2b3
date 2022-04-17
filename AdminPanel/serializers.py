from CustomizedUserModel.models import Userperson
from rest_framework import serializers

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Userperson
        fields = '__all__'
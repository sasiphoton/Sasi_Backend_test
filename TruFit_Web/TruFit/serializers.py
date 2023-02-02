from rest_framework import serializers
from .models import TFUser


class TFUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TFUser
        fields = ['name', 'email', 'role', 'created_date', 'modified_date']

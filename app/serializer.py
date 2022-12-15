from rest_framework import serializers

from app.models import *


class MarketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketer
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
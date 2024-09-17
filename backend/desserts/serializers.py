from rest_framework import serializers
from .models import Dessert, DessertCategory

class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = '__all__'
        depth = 1

class DessertCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DessertCategory
        fields = '__all__'
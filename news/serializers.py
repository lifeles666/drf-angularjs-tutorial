from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    tracks = serializers.RelatedField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent')
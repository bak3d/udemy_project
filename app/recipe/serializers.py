from rest_framework import serializers

from core.models import Tag,Ingredient

class TagSerializer(serializers.ModelSerializer):

    """serializers for tag objects"""

    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_Fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
from rest_framework import serializers

from core.models import Tag, Clothe

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

class ClotheSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clothe
        fields = ('id', 'name')
        read_only_fields = ('id',)
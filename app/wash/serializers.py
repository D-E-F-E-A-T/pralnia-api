from rest_framework import serializers

from core.models import Tag, Clothe, Wash

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

class WashSerializer(serializers.ModelSerializer):

    clothes = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Clothe.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Wash
        fields = '__all__'
        read_only_fields = ('id',)
    
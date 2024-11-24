from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'fam',
            'oct',
            'phone',
        ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'winter',
            'summer',
            'autumn',
            'spring',
        ]


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = [
            'latitude',
            'longitude',
            'height',
        ]


class PerevalImageSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = PerevalImage
        fields = [
            'data',
            'title',
        ]


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:$S', read_only=True)
    status = serializers.CharField(read_only=True)
    level = LevelSerializer(allow_null=True)
    user = UserSerializer()
    coord = CoordSerializer()
    image = PerevalImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = [
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user_id',
            'coord_id',
            'level',
            'images',
            'status',
        ]

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
    user_id = UserSerializer()
    coord_id = CoordSerializer()
    images = PerevalImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = [
            'url',
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

    def validate(self, data):
        if self.instance is not None:
            user_instance = self.instance.user_id
            user_data = data.get('user_id')
            user_fields = [
                user_instance.email == user_data.get('email'),
                user_instance.name == user_data.get('name'),
                user_instance.fam == user_data.get('fam'),
                user_instance.oct == user_data.get('ost'),
                user_instance.phone == user_data.get('phone'),
            ]
            if not all(user_fields):
                raise serializers.ValidationError({'Отклонено': 'Данные пользователя нельзя изменять'})

        return data

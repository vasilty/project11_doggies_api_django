from django.contrib.auth import get_user_model

from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'image',
            'breed',
            # 'age',
            'date_of_birth',
            'gender',
            'id',
            'intact_or_neutered',
        )
        model = models.Dog


class UserPrefSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user',
            'age',
            'gender',
            'size',
        )
        extra_kwargs = {'user': {'write_only': True}}
        model = models.UserPref

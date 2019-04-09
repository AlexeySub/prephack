from rest_framework import serializers
from api.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'userType', 'is_authenticated')
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            id=serializers.ModelSerializer.create(self, validated_data).id,
            email=validated_data['email'],
            name=validated_data['name'],
            userType=validated_data['userType'],
            is_authenticated=validated_data['is_authenticated'],
            password=make_password(validated_data['password'], salt='123'),
        )
        print(make_password('d', salt='123'))
        user.save()
        return user

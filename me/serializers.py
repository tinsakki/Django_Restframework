from rest_framework import serializers
from me.models import Snippet,CHOICES


class SnippetSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, default='')
    last_name = serializers.CharField(max_length=100, default='')
    phone_number = serializers.CharField(max_length=12)
    email = serializers.EmailField(max_length=100)
    role = serializers.ChoiceField(choices=CHOICES, default='REGULAR')


    def create(self, validated_data):
       
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_nmae = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance







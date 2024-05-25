from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import CompanyUsers, gender_choice
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
# class CompanyUsersSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=50)
#     password = serializers.CharField(max_length=50)
#     gender = serializers.ChoiceField(choices=gender_choice, default='M')
#     description = serializers.CharField(style={'base_template': 'textarea.html'})
    
#     def create(self, validated_data):
#         return CompanyUsers.objects.create(**validated_data)
    
#     def update(self, instances, validated_data):
#         instances.username = validated_data.get('username', instances.username)
#         instances.password = validated_data.get('password', instances.password)
#         instances.created_at = validated_data.get('created_at', instances.created_at)
#         instances.gender = validated_data.get('gender', instances.gender)
#         instances.description = validated_data.get('description', instances.description)
#         instances.save()
#         return instances
    
class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUsers
        fields = ['id', 'username', 'password', 'created_at', 'gender', 'description']
        

from rest_framework import serializers
from .models import Project, Client, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_at', 'updated_at', 'created_by']

class ClientDetailSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'projects']


class CreateProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True)
    users = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Project
        fields = ['name', 'client', 'users', 'created_by']

    def create(self, validated_data):
        client = validated_data.pop('client')
        users = validated_data.pop('users')
        project = Project.objects.create(client=client, **validated_data)

        # Find and assign the users by their names
        user_objects = User.objects.filter(name__in=users)
        project.users.set(user_objects)

        return project

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "project_name": instance.name,
            "client": instance.client.client_name,  # Assuming `client_name` is a field in the Client model
            "users": [
                {
                    "id": user.id,
                    "name": user.name,
                    "created_at": user.created_at.isoformat(),
                    "created_by": user.created_by
                }
                for user in instance.users.all()
            ]
        }

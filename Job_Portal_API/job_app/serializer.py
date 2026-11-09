from rest_framework import serializers
from django.contrib.auth.models import User
from job_app.models import JobModel


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobModel
        fields="__all__"
        read_only_fields=["posted_by"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username',
                'password',
                'email',
                'first_name',
                'last_name']
    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u

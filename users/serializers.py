from rest_framework import serializers

from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id',
                  'last_login',
                  'email',
                  'username',
                  'user_type',
                  'first_name',
                  'last_name',
                  'gender',
                  'created_at']

        read_only_fields = ['id']
        extra_kwargs = {
            'username': {'write_only': True}
        }

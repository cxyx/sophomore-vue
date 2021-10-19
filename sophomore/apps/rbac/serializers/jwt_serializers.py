from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from icecream import ic
from rest_framework import exceptions, serializers
from django.contrib.auth import authenticate, get_user_model
from django.db import models


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField(required=False)
        self.fields['username'] = serializers.CharField(required=False)
        self.fields['mobile'] = serializers.CharField(required=False)

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # 添加额外信息
        token['username'] = user.username
        return token

    def validate(self, attrs):
        # authenticate_kwargs = {
        #     self.username_field: attrs[self.username_field],
        #     'password': attrs['password'],
        #     # 'email':'admin@qq.com',
        #     # 'password':'admin',
        # }
        authenticate_kwargs = dict(attrs)
        ic(authenticate_kwargs)

        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        data = {}

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

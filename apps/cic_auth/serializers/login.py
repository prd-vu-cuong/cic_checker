#  Copyright (c) 2022,
#  CIC Checker
# __author = "cuong"
# __date_time = "7/24/22, 9:47 AM"

from rest_framework import serializers, status
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        write_only=True,
    )
    password = serializers.CharField(
        style=dict(input_type="password"),
        trim_whitespace=True,
        write_only=True,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username:
            message = "Username is required"
            raise serializers.ValidationError(detail=message, code="authorization")
        if not password:
            message = "Password is required"
            raise serializers.ValidationError(detail=message, code="authorization")

        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )
        if not user:
            message = "Access denied: wrong username or password."
            raise serializers.ValidationError(detail=message, code="authorization")

        setattr(attrs, "user", user)

        return attrs

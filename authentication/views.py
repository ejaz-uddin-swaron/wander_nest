from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import UserProfile


class RegisterView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'first_name', 'last_name', 'email', 'phone', 'country', 'password', 'confirm_password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
                'country': openapi.Schema(type=openapi.TYPE_STRING),
                'age': openapi.Schema(type=openapi.TYPE_INTEGER, description='Optional'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password'),
                'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, format='password')
            },
        )
    )
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password')
            },
        )
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            profile = getattr(user, 'userprofile', None)
            return Response({
                'token': token.key,
                'uid': user.id,
                'username': user.username,
                'phone': profile.phone if profile else '',
                'age': profile.age if profile else None
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Logs out user (requires token in headers)",
        responses={200: openapi.Response("Logged out")},
        security=[{'Token': []}]
    )
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'detail': 'Logged out'}, status=status.HTTP_200_OK)

# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class SignupView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to sign up

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to sign in

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = CustomUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


####################### IF WE USE DEFAULT USER MODEL ####################################

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework import status
# from django.contrib.auth.models import User
# from .serializers import UserSerializer
# from rest_framework_simplejwt.tokens import RefreshToken

# class SignupView(APIView):
#     permission_classes = [AllowAny]  # Allow anyone to sign up

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SigninView(APIView):
#     permission_classes = [AllowAny]  # Allow anyone to sign in

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # Authenticate the user
#         user = User.objects.filter(username=username).first()
#         if user and user.check_password(password):
#             # Generate JWT tokens
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'access': str(refresh.access_token),
#                 'refresh': str(refresh)
#             })
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

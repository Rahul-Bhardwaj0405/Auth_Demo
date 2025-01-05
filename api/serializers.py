# If You Need to Extend the Default User Model
# Using One-to-One Relationship: If you later need to add custom fields (like bio), you can create a related model using a one-to-one field:


from rest_framework import serializers
from .models import CustomUser  # Use the custom user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving the user
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', '')  # Handle optional bio field
        )
        return user

#################################################################################
    
    # Simplified or Refactored

# from rest_framework import serializers
# from django.contrib.auth.password_validation import validate_password
# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'password', 'bio']
#         extra_kwargs = {'password': {'write_only': True}}

#     def validate_password(self, value):
#         validate_password(value)  # Enforce Django's password validation
#         return value

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#             bio=validated_data.get('bio', '')
#         )
#         return user

####################### IF WE USE DEFAULT USER MODEL ##############################################

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}  # Ensure password is write-only
#         }

#     def validate_password(self, value):
#         # Validate password using Django's built-in validators
#         validate_password(value)
#         return value

#     def create(self, validated_data):
#         # Create a new user with a hashed password
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user

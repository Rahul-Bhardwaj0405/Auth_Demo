# If You Need to Extend the Default User Model
# Using One-to-One Relationship: If you later need to add custom fields (like bio), you can create a related model using a one-to-one field:

# python
# Copy code
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True, null=True)
# This keeps the User model unchanged while allowing you to store additional user-related data.
# Switching to a Custom User Model: If you anticipate needing custom fields frequently, you should define a custom user model from the beginning by extending AbstractUser or AbstractBaseUser. However, if you decide this later, switching to a custom user model can be more complex.

########################################################################################

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.conf import settings

class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)

#####################################################################################

# SIMPLIFIED OR REFACTORED CODE

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     bio = models.TextField(blank=True, null=True)

# Switching to a Custom User Model: If you anticipate needing custom fields frequently, you should define a custom user model from the beginning by extending AbstractUser or AbstractBaseUser. However, if you decide this later, switching to a custom user model can be more complex.


######################### IF WE USE DEFAULT USER MODEL #############################################

# from django.db import models
# from django.contrib.auth.models import User


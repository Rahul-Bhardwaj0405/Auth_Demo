from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView, SigninView

urlpatterns = [

    ########################################### API TOKEN ############################
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),

    ########################################### API TOKEN ############################
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    ######################################### USER ###################################
    path('signup/', SignupView.as_view(), name='signup'),  # For user registration
    path('signin/', SigninView.as_view(), name='signin'),  # For user login and token
]


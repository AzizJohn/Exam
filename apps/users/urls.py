from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from apps.users.api_endpoints.User import UserRegisterAPIView, LoginAPIView, LogoutAPIView
from apps.users.api_endpoints.User.User_Destroy import UserDestroyAPIView

app_name = "users"

urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),

    path("register/", UserRegisterAPIView.as_view(), name="user_register"),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('logout/', LogoutAPIView.as_view(), name='user_logout'),
    path('destroy-user/<int:pk>/', UserDestroyAPIView.as_view(), name='user_destroy'),
]

from django.urls import path
from .views import RegisterView, LoginView, UserListCreateView, ServiceListCreateView, CartListCreateView,GenderListCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path('users/', UserListCreateView.as_view(), name="users"),
    path('service/', ServiceListCreateView.as_view(), name="service"),
    path('cart/', CartListCreateView.as_view(), name="cart"),
    path('gender/', GenderListCreateView.as_view(), name="gender")
]
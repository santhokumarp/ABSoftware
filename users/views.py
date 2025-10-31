from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Login, Gender, Role, Service, Users, Cart
from .serializers import RegisterSerializer, LoginSerializer, GenderSerializer, RoleSerializer, ServiceSerializer, UserSerializer, CartSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            # ✅ Check user by username or email
            user = Login.objects.filter(username=username).first()
            if not user:
                user = Login.objects.filter(email=username).first()

            # ✅ Handle user not found
            if not user:
                return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

            # ✅ Verify password
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "Login successful",
                    "username": user.username,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenderListCreateView(APIView):
    def get(self, request):
        gender = Gender.objects.all()
        serializer = GenderSerializer(gender, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class ServiceListCreateView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serailizer = ServiceSerializer(services, many=True)
        return Response(serailizer.data)
    
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class UserListCreateView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = ServiceSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CartListCreateView(APIView):
    def get(self,request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    





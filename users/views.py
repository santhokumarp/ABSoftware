from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            try:
                # user = User.objects.get(username=username) or User.objects.get(email=username)
                user = User.objects.filter(username=username).first()
                if not user:
                     user = User.objects.filter(email= username).first()

            except User.DoesNotExist:
                return Response({"error": "invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
            if user.check_password(password):
                return Response({
                    "message": "Login successful",
                    "username" : user.username,
                    "role": user.role,
                },status=status.HTTP_200_OK)
            else:
                return Response({
                    "error":"Invalid username or password"
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
              
            




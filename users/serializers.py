from rest_framework import serializers
from .models import Gender, Role, Service, Users, Cart ,Login

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['username','email','password','password2','role']
        extra_kwargs = {
            'role': {'read_only': True},
            'password': {'write_only': True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"passwords do not match"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = Login(**validated_data)
        user.set_password(password)
        user.role = 'user'
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False , allow_blank = True)
    email = serializers.CharField(required=False , allow_blank = True)
    password = serializers.CharField(write_only=True)

# class GenderSerializer(serializers.ModelSerializer):
#     class meta:
#         model = Gender
#         field = '__all__'

# class RoleSerializer(serializers.ModelSerializer):
#     class meta:
#         model = Role
#         field = '__all__'

# class ServiceSerializer(serializers.ModelSerializer):
#     class meta:
#         model = Service
#         field = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class meta:
#         model = Users
#         field = '__all__'

# class CartSerializer(serializers.ModelSerializer):
#     class meta:
#         model = Cart
#         field = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:  # <-- FIX: Changed 'meta' to 'Meta'
        model = Gender
        fields = '__all__' # FIX: Changed 'field' to 'fields'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:  # <-- FIX: Changed 'meta' to 'Meta'
        model = Role
        fields = '__all__' # FIX: Changed 'field' to 'fields'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:  # <-- FIX: Changed 'meta' to 'Meta'
        model = Service
        fields = '__all__' # FIX: Changed 'field' to 'fields'

class UserSerializer(serializers.ModelSerializer):
    class Meta:  # <-- FIX: Changed 'meta' to 'Meta'
        model = Users
        fields = '__all__' # FIX: Changed 'field' to 'fields'

class CartSerializer(serializers.ModelSerializer):
    class Meta:  # <-- FIX: Changed 'meta' to 'Meta'
        model = Cart
        fields = '__all__' # FIX: Changed 'field' to 'fields'








    

        

    







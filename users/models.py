from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class UserRole(models.TextChoices):
    ADMIN = 'admin','Admin'
    # PROVIDER = 'provider', 'Provider'
    USER = 'user','User'

class Login(models.Model):
    username = models.CharField(max_length=100, unique=True, )
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)
    date_joined = models.DateTimeField(default=timezone.now)

    USER_FIELD = 'username'
    REQUIRED_FIELDS =['email']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def __str__(self):
        return f"{self.username} ({self.role})"
# class Service(models.Model):
#     services = models.CharField(max_length=100)
#     services_Id = models.IntegerField()
#     servicesType = models.CharField(max_length=100)
#     servicesType_id = 
class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.gender_name


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.role_name
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.service_name

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null= True)
    choose_time = models.TimeField(null=True, blank=True)
    choose_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Assign default role if not provided
        if not self.role:
            default_role, created = Role.objects.get_or_create(role_name='User')
            self.role = default_role
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default='pending')
    payment = models.CharField(max_length=50, default="unpaid")
    date_created = models.DateField(auto_now_add=True)
    time_creaded = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.service_name}"

class Booking(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, default='paid')
    status = models.CharField(max_length=50, default='confirmed')

    def __str__(self):
        return f"Booking: {self.user} - {self.service}"






    
    







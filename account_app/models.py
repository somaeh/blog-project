from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nationalcode=models.CharField(max_length=10)
    name_father=models.CharField(max_length=25)
    image=models.ImageField(upload_to="profiles/images", blank=True, null=True)
    
    
    
    def __str__(self):
        return self.user.username
















# class Profile_user(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     father_name=models.CharField(max_length=27)
#     national_code=models.CharField(max_length=10)
#     image=models.ImageField(upload_to="profiles/images")
    
    
#     def __str__(self):
#         return self.user.username

















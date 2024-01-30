from django.db import models

# Create your models here.

class usertable(models.Model):
    Maleorfemale=[('male', 'Male'), ('female', 'Female')]
    
    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10, choices=Maleorfemale)
    password = models.CharField(max_length=100,null=True)
    confirm_password = models.CharField(max_length=100,null=True)
    pimage = models.ImageField(null=True,blank=True,upload_to="images/")
    
    def __str__(self):
        return self.username
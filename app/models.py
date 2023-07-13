from django.db import models
from django.contrib.auth.models import User

class myprofile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=250,default="Male")
    added_on =models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    gender = models.CharField(max_length=250,default="Male")

    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
       return self.email
    
class levent1(models.Model):
    line1 = models.CharField(max_length=25,default="levent1")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="levent1/",null=True,blank=True) 

    def __str__(self):
        return self.line1
    
class levent2(models.Model):
    line1 = models.CharField(max_length=25,default="levent2")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="levent2/",null=True,blank=True) 

    def __str__(self):
        return self.line1

class levent3(models.Model):
    line1 = models.CharField(max_length=25,default="levent3")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="levent3/",null=True,blank=True) 

    def __str__(self):
        return self.line1    

class levent4(models.Model):
    line1 = models.CharField(max_length=25,default="levent4")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="levent4/",null=True,blank=True) 

    def __str__(self):
        return self.line1
    
class uevent1(models.Model):
    line1 = models.CharField(max_length=25,default="uevent1")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="uevent1/",null=True,blank=True) 

    def __str__(self):
        return self.line1 

class uevent2(models.Model):
    line1 = models.CharField(max_length=25,default="uevent2")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="uevent2/",null=True,blank=True) 

    def __str__(self):
        return self.line1

class uevent3(models.Model):
    line1 = models.CharField(max_length=25,default="uevent3")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="uevent3/",null=True,blank=True) 

    def __str__(self):
        return self.line1

class uevent4(models.Model):
    line1 = models.CharField(max_length=25,default="uevent4")
    line2 = models.CharField(max_length=25,null=True,blank=True)
    line3 = models.CharField(max_length=25,null=True,blank=True)
    image = models.ImageField(upload_to="uevent4/",null=True,blank=True) 

    def __str__(self):
        return self.line1
    
class platinumcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    stage = models.CharField(max_length=500, default='Platinum Stage')
    ticketqty = models.IntegerField(default=1)
    ticketprice = models.IntegerField(default=1500)
    title = models.CharField(max_length=500, default="Rockstar Anirudh Music Festival")
    language = models.CharField(max_length=500, default="Tamil")
    rated = models.CharField(max_length=500, default="U/A Family Friendy")
    date = models.CharField(max_length=500,default="April 5 | 10AM")
    locate = models.CharField(max_length=500,default="Jawaharlal Nehru Stadium | Chennai")
    ispaid = models.BooleanField(default=False)
    qrcode = models.FileField(null=True,blank=True)

class goldcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    stage = models.CharField(max_length=500, default='Gold Stage')
    ticketqty = models.IntegerField(default=1)
    ticketprice = models.IntegerField(default=1000)
    title = models.CharField(max_length=500, default="Rockstar Anirudh Music Festival")
    language = models.CharField(max_length=500, default="Tamil")
    rated = models.CharField(max_length=500, default="U/A Family Friendy")
    date = models.CharField(max_length=500,default="April 5 | 10AM")
    locate = models.CharField(max_length=500,default="Jawaharlal Nehru Stadium | Chennai")
    ispaid = models.BooleanField(default=False)

class generalcart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    stage = models.CharField(max_length=500, default='General Stage')
    ticketqty = models.IntegerField(default=1)
    ticketprice = models.IntegerField(default=500)
    title = models.CharField(max_length=500, default="Rockstar Anirudh Music Festival")
    language = models.CharField(max_length=500, default="Tamil")
    rated = models.CharField(max_length=500, default="U/A Family Friendy")
    date = models.CharField(max_length=500,default="April 5 | 10AM")
    locate = models.CharField(max_length=500,default="Jawaharlal Nehru Stadium | Chennai")
    ispaid = models.BooleanField(default=False)

class msg(models.Model):
    msg = models.CharField(max_length=1000,default='Invalid Username or Password')

    def __str__(self):
        return self.msg    
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User=get_user_model()

class Todo(models.Model):
    user_name=models.ForeignKey(User,related_name="todos",on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    send_alert=models.BooleanField(default=False)
    date_time=models.DateTimeField()

class Profile(models.Model):
    user=models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    location=models.TextField()
    contact=models.IntegerField()

# class License(models.Model):

# if settings.DEBUG:
    # urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    

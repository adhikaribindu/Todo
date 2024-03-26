from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Attendance(models.Model):
    user_name=models.ForeignKey(User,related_name='app',on_delete=models.CASCADE)
    checkin_date=models.DateField()
    check_in=models.TimeField()
    check_out=models.TimeField()

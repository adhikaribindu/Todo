from rest_framework.response import Response
from rest_framework.views import APIView
from attendance.models import Attendance
from .serializers import AttendanceSerializers,UserSerializers
from django.contrib.auth import get_user_model


User=get_user_model()
class TestAPIView(APIView):
    def get(self,request,*args, **kwargs):
        queryset=Attendance.objects.all()
        response_={
            "data":{
                "name":"Bindu"
            }
        }
        serializers=AttendanceSerializers(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request,*args,**kwargs):
        serializer =AttendanceSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response({"message":"Data saved"})
    

class UserAPIView(APIView):
    def get(self,request,*args,**kwargs):
        users=User.objects.all()
        serialiizers=UserSerializers(users,many=True)
        return Response(serialiizers.data)
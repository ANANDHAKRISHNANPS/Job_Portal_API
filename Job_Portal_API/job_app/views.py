from django.conf.locale import sr
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.templatetags import rest_framework
from rest_framework.views import APIView

from job_app import serializer
from job_app.serializer import JobSerializer,UserSerializer
from rest_framework import status
from job_app.models import JobModel
from job_app.permission import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer_instances=UserSerializer(data=request.data)
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response(serializer_instances.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instances.errors)

class CreateViewJob(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        serializer_instances=JobSerializer(data=request.data)
        if serializer_instances.is_valid():
            serializer_instances.save(posted_by=request.user)
            return Response(serializer_instances.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        j=JobModel.objects.all()
        serializer_instances=JobSerializer(j,many=True)
        return Response(serializer_instances.data,status=status.HTTP_200_OK)

class RetrieveUpdateDeleteJob(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    def get(self,request,i):
        j=get_object_or_404(JobModel,id=i)
        self.check_object_permissions(request,j)
        serializer_instances=JobSerializer(j)
        return Response(serializer_instances.data,status=status.HTTP_200_OK)

    def put(self,request,i):
        j=get_object_or_404(JobModel,id=i)
        self.check_object_permissions(request,j)
        serializer_instances = JobSerializer(j,data=request.data)
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response(serializer_instances.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instances.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,i):
        j=get_object_or_404(JobModel,id=i)
        self.check_object_permissions(request,j)
        j.delete()
        return Response({'message':'Deletion successfull'})


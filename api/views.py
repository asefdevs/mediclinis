from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import News
from .serializer import NewsGetSerializer,NewsPostSerializer,SubscribeSerializer

class NewsView(APIView):
    def get(self, request):
        news=News.objects.filter(is_active=True)
        serializer=NewsGetSerializer(news,many=True,context={'request':request})

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=NewsPostSerializer(data=request.data, context={'request':request}) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:   
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class NewsDetailView(APIView):
    def get(self, request,id):
        try:
            news=News.objects.get(id=id)
            serializer=NewsGetSerializer(news,context={'request':request})
            return Response(serializer.data,status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data={'message':'news not found'})
    
    def put(self,request,id):
        try:
            news=News.objects.get(id=id)
            serializer=NewsPostSerializer(news,data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data={'error':'not found'})

class SubscriberView(APIView):
    serializer_class = SubscribeSerializer
    
    def post(self, request):
        serializer=SubscribeSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
# Create your views here.



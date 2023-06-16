from rest_framework import routers, serializers
from core.models import News,Category,Subscriber


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['title']


class NewsPostSerializer(serializers.ModelSerializer):
    # category=CategoryGetSerializer()

    class Meta:
        model=News
        fields=['title', 'content', 'image', 'category',]


class NewsGetSerializer(serializers.ModelSerializer):
    category=CategoryGetSerializer()

    class Meta:
        model=News
        fields=['title', 'content', 'image',  'created_at','category',]


class SubscribeSerializer(serializers.ModelSerializer):
   class Meta:
    
    model=Subscriber
    fields=['email']


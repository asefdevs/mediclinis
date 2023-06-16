from django.urls import path

from .views import (
    NewsView,
    NewsDetailView,
    SubscriberView

    )

urlpatterns =[
    path('news/',NewsView.as_view(),name='news'), 
    path('news/<int:id>/',NewsDetailView.as_view(),name='news_detail'),
    path('subscriber/',SubscriberView.as_view(),name='subscriber')

]
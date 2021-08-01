from django.urls import path
from .views import MobileView,MobileDetailView


urlpatterns=[
    path('',MobileView.as_view(), name='mobile_view'),
    path('<int:pk>',MobileDetailView.as_view(), name='mobile_details')
]
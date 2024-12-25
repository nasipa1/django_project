from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionList

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('transactions/', TransactionList.as_view(), name='transactions'),

]

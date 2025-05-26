from django.urls import path
from django.http import HttpResponse
from .views import FoodItemList, FoodItemDetail, OrderListCreate, OrderDetail

def api_root(request):
    return HttpResponse("Welcome to the API. Try /api/foods/ or /api/orders/")

urlpatterns = [
    path('', api_root, name='api-root'),  # Handles /api/
    path('foods/', FoodItemList.as_view(), name='food-list'),
    path('foods/<int:pk>/', FoodItemDetail.as_view(), name='food-detail'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]


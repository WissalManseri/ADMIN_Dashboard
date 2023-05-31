from django.urls import path
from .views import DashboardView, UserListView, OrderListView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]

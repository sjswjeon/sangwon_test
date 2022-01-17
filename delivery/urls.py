from django.urls import path
from delivery import views

urlpatterns = [
    # path('orders/<int:shop>', views.order_list, name="order_list"),
    path('orders/', views.order_list, name='order_list'),
]

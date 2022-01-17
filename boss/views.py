from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def order_list(request, shop):
    if request.method == 'GET':
        # order_list = Order.objects.all()
        order_list = Order.objects.filter(shop = shop)
        return render(request, 'boss/order_list.html', { 'order_list' : order_list })

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        order = Order.objects.get(pk = int(request.POST['order_id']))
        shop = order.shop
        order.estimated_time = int(request.POST['estimated_time'])
        order.save()
        return render(request, 'boss/success.html', { 'shop' : shop })
    else:
        return HttpResponse(status=404)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        # order_list = Order.objects.all()
        order_list = Order.objects.all()
        return render(request, 'delivery/order_list.html', { 'order_list' : order_list })

    elif request.method == 'POST':
        order = Order.objects.get(pk = int(request.POST['order_id']))
        order.deliver_finish = True
        order.save()
        return render(request, 'delivery/success.html')

from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from django.http import JsonResponse
from django.conf import settings
from .models import Item
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def item(request, pk):
    context = {
        'item': Item.objects.get(id=pk),
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'app/item.html', context)

class Buy(View):
    def post(self, request, pk):
        item = Item.objects.get(id=pk)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        # YOUR_DOMAIN = "https://testtask02.herokuapp.com"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            "description": item.description,
                        },
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/item/' + str(item.id),
            cancel_url=YOUR_DOMAIN + '/item/' + str(item.id),
        )
        return JsonResponse({
            'id': checkout_session.id
        })

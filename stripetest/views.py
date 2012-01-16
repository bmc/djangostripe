from django.template import RequestContext, Context, loader
from stripetest.models import CustomerInfo, Product
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
import settings

@login_required
def index(request):
    context = Context({
        'products': Product.objects.all(),
        'user':     request.user
    })
    return render_to_response('stripetest/index.html', context)

@login_required
def buy(request):
    # Request is assumed to be a POST.

    # Get the Stripe token.
    stripe_token = request.POST['stripeToken']

    # Set the Stripe secret key. This is currently the test key for Brian
    # Clapper. See https://manage.stripe.com/account/
    stripe.api_key = 'U0rEoxN4XTw1uKTBn0a8He9ITVQgBvVd'

    # Create the carge on Stripe's servers. This will charge the card.
    product = Product.objects.get(id=id)
    charge = stripe.Charge.create(
        amount      = product.price_in_cents(),
        currency    = 'usd',
        card        = stripe_token,
        description = 'Customer bought %s' % product.name
    )

    return render_to_response('stripetest/products.html', c)

@login_required
def product(request, id):
    product = Product.objects.get(id=id)
    context = Context({
        'product': product,
        'user':    request.user
    })
    return render_to_response('stripetest/product.html', context)

def force_logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

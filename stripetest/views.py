from django.template import RequestContext, Context, loader
from stripetest.models import CustomerChargeData, Product, Purchase
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
import settings
import stripe

@login_required
def index(request):
    context_hash = {
        'products': Product.objects.all(),
        'user':     request.user
    }
    context_hash.update(common_context_hash(request))
    return render_to_response(
      'stripetest/index.html', RequestContext(request, context_hash)
    )

@login_required
def buy(request):
    # Get the Stripe token associated with the credit card details.
    stripe_token = request.POST['stripeToken']

    # Set the Stripe secret key. This is currently the test key for Brian
    # Clapper. See https://manage.stripe.com/account/
    stripe.api_key = settings.STRIPE_API_KEY

    user = request.user

    # Get other parameters.
    card_last4 = request.POST['card_last4']
    card_type  = request.POST['card_type']

    # Determine if we have a local customer record for this user and card. If
    # not, we'll create one and create a stripe customer. NOTE: A Stripe
    # "Customer" appears to be associated with one and only one credit card.
    # So, our data model keeps multiple CustomerChargeData records per user,
    # one for each card.
    card_data = CustomerChargeData.objects.filter(
        user = user, card_type = card_type, card_last4 = card_last4
    )
    if len(card_data) == 0:
        # Create Stripe customer.
        stripe_customer = stripe.Customer.create(
            card = stripe_token,
            description = "Striped customer for %s " % user.email,
            email = user.email
        )

        # Create a corresponding local record.
        local_customer = CustomerChargeData(
            user = user,
            stripe_customer_id = stripe_customer.id,
            card_type = card_type,
            card_last4 = card_last4
        )
        local_customer.save()

    else:
        # We have this card already.
        local_customer = card[0]

        # Get the corresponding Stripe customer. NOTE: We assume lockstep
        # data here, which is probably a bad idea in a production system.
        # But this is just a demo...
        stripe_customer = stripe.Customer.retrieve(
            local_customer.stripe_customer_id
        )

    # Create the charge on Stripe's servers. This will charge the card.
    product = Product.objects.get(id=request.POST['product_id'])
    charge = stripe.Charge.create(
        amount      = product.price_in_cents(),
        currency    = 'usd',
        customer    = stripe_customer.id,
        description = '%s bought %s' % (user.email, product.name)
    )

    # Record the purchase locally.
    purchase = Purchase(product=product, user=user)
    purchase.save()

    context_hash = {
        'card_last4': card_last4,
        'card_type':  card_type,
        'user':       request.user,
        'product':    product
    }
    context_hash.update(common_context_hash(request))
    return render_to_response(
        'stripetest/receipt.html', RequestContext(request, context_hash)
    )

@login_required
def product(request, id):
    product = Product.objects.get(id=id)
    context_hash = {
        'product': product,
        'user':    request.user
    }
    context_hash.update(common_context_hash(request))
    return render_to_response(
        'stripetest/product.html', RequestContext(request, context_hash)
    )

def force_logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def common_context_hash(request):
    return {
        'user': request.user,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    }

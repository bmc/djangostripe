from django.template import Context, loader
from stripetest.models import Customer, Product
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    c = Context({
        'products': Product.objects.all(),
    })
    return render_to_response('stripetest/index.html', c)

def products(request):
    c = Context({
        'title': 'This is a test',
    })
    return render_to_response('stripetest/products.html', c)

def product(request, id):
    p = Product.objects.get(id=id)
    print '*** %s' % str(p)
    c = Context({
        'product': p,
    })
    return render_to_response('stripetest/product.html', c)

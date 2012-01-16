from django.template import Context, loader
from stripetest.models import Customer
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    t = loader.get_template('stripetest/index.html')
    c = Context({
        'title': 'This is a test',
    })
    return render_to_response('stripetest/index.html', c)

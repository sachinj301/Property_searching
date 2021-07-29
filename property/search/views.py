from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

def index(request):
    list = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtor = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtor,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
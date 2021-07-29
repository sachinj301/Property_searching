from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices
from django.db.models import Q


def index(request):
    list = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(list, 3)
    page = request.GET.get('page')
    paged_list = paginator.get_page(page)
    content = {
        'listings': paged_list
    }
    return render(request, 'listings/listings.html', content)

def listing(request,id):
    listing = get_object_or_404(Listing, pk=id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            queryset_list = queryset_list.filter(description__icontains=keyword)

    if 'city' in request.GET:
        cities = request.GET['city']
        if cities:
            print(cities)
            queryset_list = queryset_list.filter(city__iexact=cities)

    if 'state' in request.GET:
        states = request.GET['state']
        if states:
            print('state view', states)
            queryset_list = queryset_list.filter(state__iexact=states)
            print('queryset', queryset_list)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        prices = request.GET['price']
        if prices:
            queryset_list = queryset_list.filter(price__lte=prices)

    context = {
        'listings': queryset_list,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'values': request.GET,

    }
    return render(request, 'listings/search.html', context)

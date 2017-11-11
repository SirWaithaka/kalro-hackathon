from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from .utils import get_goats,get_broodsites,get_irrigationforage,get_amaranthgroups,get_weanercalves,get_weightgains,get_weightgainbenefit


def goats_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        goats = get_goats(query=q)
    else:
        goats = get_goats()

    data = []
    for goat in goats['data']:
        data.append(goat)

    context = {
        'goats':data
    }
    return render(request, 'goats.html', context)


def irrigationforage_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        irrigationforage = get_irrigationforage(query=q)
    else:
        irrigationforage = get_irrigationforage()

    data = []
    for irrigation in irrigationforage['irrigationforage']:
        data.append(irrigation)

    context = {
        'irrigationforage': data
    }
    return render(request, 'irrigationforage.html', context)


def home(request):
    return render(request,'index.html')

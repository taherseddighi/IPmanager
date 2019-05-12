from django.shortcuts import render
from json import JSONEncoder
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Available_Public_IP


# Create your views here.

@csrf_exempt
def submit_Available_Public_IP(request):
    #validate data later
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if request.POST['date_start']:
        Available_Public_IP.objects.create(user=this_user, IP=request.POST['IP'], date_start=request.POST['date_start'], date_expire=request.POST['date_expire'], price_bought=request.POST['price_bought'], price_to_sell=request.POST['price_to_sell'], description=request.POST['description'])
    else:
        now = datetime.now()
        Available_Public_IP.objects.create(user=this_user, IP=request.POST['IP'], date_start=now, date_expire=request.POST['date_expire'], price_bought=request.POST['price_bought'], price_to_sell=request.POST['price_to_sell'], description=request.POST['description'])
    print('HI Can you See Me ? I am Here. Holllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(request.POST)

    return JsonResponse({
        'status':'ok',
    }, encoder=JSONEncoder)
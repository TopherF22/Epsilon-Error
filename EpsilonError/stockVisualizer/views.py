from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StockData

import requests
import json


APIKEY = 'UTJYXBQOKRCYNWXR' 
#replace 'my_alphav_api_key' with your actual Alpha Vantage API key obtained from https://www.alphavantage.co/support/#api-key


DATABASE_ACCESS = False 
#if False, the app will always query the Alpha Vantage APIs regardless of whether the stock data for a given ticker is already in the local database


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

@csrf_exempt
def get_stock_data(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        ticker = request.POST.get('ticker', 'null')
        ticker = ticker.upper()

        if DATABASE_ACCESS == True:
            #checking if the database already has data stored for this ticker before querying the Alpha Vantage API
            if StockData.objects.filter(symbol=ticker).exists(): 
                entry = StockData.objects.filter(symbol=ticker)[0]
                return HttpResponse(entry.data, content_type='application/json')

        output_dictionary = {}


        response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={APIKEY}&outputsize=full')
        print(response.status_code)
        price_series = response.json()
        print(price_series)
        # price_series = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={APIKEY}&outputsize=full').json()



        response = requests.get(f'https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period=10&series_type=close&apikey={APIKEY}')
        sma_series = response.json()
        # sma_series = requests.get(f'https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period=10&series_type=close&apikey={APIKEY}').json()

        output_dictionary['prices'] = price_series['Time Series (Daily)']
        output_dictionary['sma'] = sma_series['Technical Analysis: SMA']

        temp = StockData(symbol=ticker, data=json.dumps(output_dictionary))
        temp.save()

        return HttpResponse(json.dumps(output_dictionary), content_type='application/json')

    else:
        message = "Not Ajax"
        return HttpResponse(message)
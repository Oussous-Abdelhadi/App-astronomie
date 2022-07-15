import imp
from django.http import HttpResponse
from django.shortcuts import render
import requests
import datetime
from googletrans import Translator  

# Create your views here.
from datetime import datetime
def index(request):
    context = {}
    print(datetime.now())
    context["data"] = 1
    return render(request, 'space/index.html', context=context)

def apiNasa(request):
    date = request.POST.get("date-time")
    key = "zmyT1mibIhnrYPwcuy5dY4wjjWGRO6eZvXofwXau"
    data_date = date
    api_lien = f"https://api.nasa.gov/planetary/apod?date={data_date}&api_key={key}"

    data = requests.get(api_lien).json()
    text = data["explanation"]
    translator = Translator()
    translation = translator.translate(text, dest='fr')
    explication = translation.text 
    # print(explanation)
    return render(request, 'space/space_data.html', {'data': data , 'date':date, 'explication': explication})
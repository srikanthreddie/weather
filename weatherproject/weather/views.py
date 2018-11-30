from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def showIndex(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d44586d3b0fd0e47776362801b1ddfaa'
    city = 'Bengaluru'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()

    weather_data=[]

    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather = {
            'city' : city,
            'temperature' :r['main']['temp'],
            'description' :r['weather'][0]['description'],
            'icon' :r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    data={'weather_data':weather_data,'form':form}
    print(data)
    return render(request,"weather.html",data)
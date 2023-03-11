import requests as req
from api_key import API_key
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
from rich.table import Table
from weather_pics import weatherIcon

console = Console()
console.print(Panel.fit("[bold red]Weather",border_style='red'))
layout=Layout()
layout.split_row(
    Layout(name='left'),
    Layout(name='right'),
    
)
api_key=API_key()

def weatherPrint(temp_units,lat,lon,api_key,city_json) :
    if temp_units=='1':
        weth_req=req.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}')
        weth_json=weth_req.json()        
        weatherprint=Table.grid(padding=2)
        weatherprint.add_column(style='blue',justify='left')
        weatherprint.add_column(no_wrap=True)
        weatherprint.add_row( f'''
        [bold]City: [/bold]{city_json[0]['name']}
        [bold]Weather: [/bold]{weth_json['weather'][0]['main']}
        [bold]Description: [/bold]{weth_json["weather"][0]['description']}
        [bold]Tempetur: [/bold]{str(weth_json['main']['temp'])} C
        [bold]Feels like: [/bold]{str(weth_json['main']['feels_like'])} C
        [bold]Tempetur minimum: [/bold]{str(weth_json['main']['temp_min'])} C
        [bold]Tempetur max: [/bold]{str(weth_json['main']['temp_max'])} C
        [bold]Pressuer: [/bold]{str(weth_json['main']['pressure'])} hPa
        [bold]Humidity: [/bold]{str(weth_json['main']['humidity'])}%''')
        state_icon=str(weth_json['weather'][0]['main'])
        layout['right'].update(weatherprint)
        layout['left'].update(weatherIcon(weth_json))
        print(layout)
    if temp_units=='2':
        weth_req=req.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}')
        weth_json=weth_req.json() 
        weatherprint=Table.grid(padding=2)
        weatherprint.add_column(style='blue',justify='left')
        weatherprint.add_column(no_wrap=True)
        weatherprint.add_row( f'''
        [bold]City: [/bold]{city_json[0]['name']}
        [bold]Weather: [/bold]{weth_json['weather'][0]['main']}
        [bold]Description: [/bold]{weth_json["weather"][0]['description']}
        [bold]Tempetur: [/bold]{str(weth_json['main']['temp'])} F
        [bold]Feels like: [/bold]{str(weth_json['main']['feels_like'])} F
        [bold]Tempetur minimum: [/bold]{str(weth_json['main']['temp_min'])} F
        [bold]Tempetur max: [/bold]{str(weth_json['main']['temp_max'])} F
        [bold]Pressuer: [/bold]{str(weth_json['main']['pressure'])} hPa
        [bold]Humidity: [/bold]{str(weth_json['main']['humidity'])}%''')
        layout['right'].update(weatherprint)
        layout['left'].update(weatherIcon(weth_json))
        print(layout)
    

def main(api_key):
    city=input('Input city name: ')
    temp_units=input('1 for metric 2 for imperial ')
    city_req=req.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}')
    city_json=city_req.json()
    lat=str(city_json[0]['lat'])
    lon=str(city_json[0]['lon'])

    weatherPrint(temp_units,lat,lon,api_key,city_json)


main(api_key)
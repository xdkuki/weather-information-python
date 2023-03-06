import requests as req
from rich import print
from rich.panel import Panel
from rich.console import Console, Group
from rich.theme import Theme
from rich.layout import Layout
from rich.table import Table
from rich.align import Align
from rich import box

console = Console()
console.print(Panel.fit("[bold red]OpenWeather API",border_style='red'))
layout=Layout()
layout.split_row(
    Layout(name='left'),
    Layout(name='right'),
    
)
print(layout)
api_key='a8d33780a6f0298df2a9dd731bd6b09d'
#def test():
#    testprint=Table.grid(padding=1)
#    testprint.add_column(style='red')
#    testprint.add_column(no_wrap=True)
#    testprint.add_row(''' 
#    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⠆⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⠄⣈⣁⠀⠻⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⣀⣤⣴⣿⠿⠛⠉⠀⠀⣿⣿⠀⠀⠀⠈⠙⠿⣷⣤⡀⠀⠀⠀⠀⠀
#⠀⠀⠀⠒⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠙⠻⣄⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀
#    
#    ''')
#    return testprint
#    print(layout['left'])
def weatherPrint(temp_units,lat,lon,api_key,city_json) :
    if temp_units==1:
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
        [bold]Feels like: [/bold]{str(weth_json['main']['feels_like'])}
        [bold]Tempetur minimum: [/bold]{str(weth_json['main']['temp_min'])}
        [bold]Tempetur max: [/bold]{str(weth_json['main']['temp_max'])}
        [bold]Pressuer: [/bold]{str(weth_json['main']['pressure'])}
        [bold]Humidity: [/bold]{str(weth_json['main']['humidity'])}''')
        layout['right'].update(weatherprint)
        print(layout)
    if temp_units==2:
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
        [bold]Feels like: [/bold]{str(weth_json['main']['feels_like'])}
        [bold]Tempetur minimum: [/bold]{str(weth_json['main']['temp_min'])}
        [bold]Tempetur max: [/bold]{str(weth_json['main']['temp_max'])}
        [bold]Pressuer: [/bold]{str(weth_json['main']['pressure'])}
        [bold]Humidity: [/bold]{str(weth_json['main']['humidity'])}''')
        layout['right'].update(weatherprint)
        print(layout)
    else:
        print('You didn\'t choose one of the options')



def main(api_key):
    city=input('Input city name: ')
    temp_units=input('1 for metric 2 for imperial ')
    city_req=req.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}')
    city_json=city_req.json()
    lat=str(city_json[0]['lat'])
    lon=str(city_json[0]['lon'])

    weatherPrint(temp_units,lat,lon,api_key,city_json)

#if temp_units=='1':
#    weth_req=req.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}')
#    weth_json=weth_req.json()
#    weatherPrint()
#elif temp_units=='2':
#    weth_req=req.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}')
#    weth_json=weth_req.json()
#    #layout['left'].update(test())
#    layout['right'].update(weatherPrint())
#    print(layout)
#    #test()


main(api_key)
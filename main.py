import requests as req
from api_key import API_key
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
api_key=API_key()


def weatherIcon(weth_json):
    weathicon=weth_json['weather'][0]['main']
    if weathicon=='Rain' or weathicon=='Drizzle':
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''
                             000      00
                           0000000   0000
              0      00  00000000000000000
            0000 0  000000000000000000000000       0
         000000000000000000000000000000000000000 000
        0000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / /

           ''')
        return weathericon
    elif weathicon=='Clear':
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''
          .      '      .
    .      .     :     .      .
     '.        ______       .'
       '  _.-"`      `"-._ '
        .'                '.
 `'--. /                    \ .--'`
      /                      \
     ;                        ;
- -- |                        | -- -
     |     _.                 |
     ;    /__`A   ,_          ;
 .-'  \   |= |;._.}{__       /  '-.
    _.-""-|.' # '. `  `.-"{}<._
          / 1938  \     \  x   `"
     ----/         \_.-'|--X----
     -=_ |         |    |- X.  =_
    - __ |_________|_.-'|_X-X##
         `'-._|_|;:;_.-'` '::.  `"-
     .:;.      .:.   ::.     '::.
           ''')
        return weathericon
    elif weathicon=='Clouds':
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''
                _                                  
              (`  ).                   _           
             (     ).              .:(`  )`.       
)           _(       '`.          :(   .    )      
        .=(`(      .   )     .--  `.  (    ) )      
       ((    (..__.:'-'   .+(   )   ` _`  ) )                 
`.     `(       ) )       (   .  )     (   )  ._   
  )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
)  )  ( )       --'       `- __.'         :(      )) 
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'          
                                        
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.
           ''')
        return weathericon
    elif weathicon=='Snow' or weathicon=='snow':
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''
                     *  .  *
                   . _\/ \/_ .
                    \  \ /  /             .      .
      ..    ..    -==>: X :<==-           _\/  \/_
      '\    /'      / _/ \_ \              _\/\/_
        \\//       '  /\ /\  '         _\_\_\/\/_/_/_
   _.__\\\///__._    *  '  *            / /_/\/\_\ \
    '  ///\\\  '                           _/\/\_
        //\\                               /\  /\
      ./    \.             ._    _.       '      '
      ''    ''             (_)  (_)                  <> \  / <>
                            .\::/.                   \_\/  \/_/
           .:.          _.=._\\//_.=._                  \\//
      ..   \o/   ..      '=' //\\ '='             _<>_\_\<>/_/_<>_
      :o|   |   |o:         '/::\'                 <> / /<>\ \ <>
       ~ '. ' .' ~         (_)  (_)      _    _       _ //\\ _
           >O<             '      '     /_/  \_\     / /\  /\ \
       _ .' . '. _                        \\//       <> /  \ <>
      :o|   |   |o:                   /\_\\><\\ \/
           ':'        . ~~\  /~~ .       _//\\_
                      _\_._\/_._/_      \_\  /_/
                       / ' /\ ' \                   \o/
       o              ' __/  \__ '              _o/.:|:.\o_
  o    :    o         ' .'|  |'.                  .\:|:/.
    '.\'/.'                 .                 -=>>::>o<::<<=-
    :->@<-:                 :                   _ '/:|:\' _
    .'/.\'.           '.___/*\___.'              o\':|:'/o
  o    :    o           \* \ / */                   /o\
       o                 >--X--<
                        /*_/ \_*\
                      .'   \*/   '.
                            :
           ''')
        return weathericon
    elif weathicon==' Thunderstorm':
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''

     .edee...      .....       .eeec.   ..eee..
   .d*"  """"*e..d*"""""**e..e*""  "*c.d""  ""*e.
  z"           "$          $""       *F         **e.
 z"             "c        d"          *.           "$.
.F                        "            "            'F
d                                                   J%
3         .                                        e"
4r       e"              .                        d"
 $     .d"     .        .F             z ..zeeeeed"
 "*beeeP"      P        d      e.      $**""    "
     "*b.     Jbc.     z*%e.. .$**eeeeP"
        "*beee* "$$eeed"  ^$$$""    "
                 '$$.     .$$$c
                  "$$.   e$$*$$c
                   "$$..$$P" '$$r
                    "$$$$"    "$$.           .d
        z.          .$$$"      "$$.        .dP"
        ^*e        e$$"         "$$.     .e$"
          *b.    .$$P"           "$$.   z$"
           "$c  e$$"              "$$.z$*"
            ^*e$$P"                "$$$"
              *$$                   "$$r
              '$$F                 .$$P
               $$$                z$$"
               4$$               d$$b.
               .$$%            .$$*"*$$e.
            e$$$*"            z$$"    "*$$e.
           4$$"              d$P"        "*$$e.
           $P              .d$$$c           "*$$e..
          d$"             z$$" *$b.            "*$L
         4$"             e$P"   "*$c            ^$$
         $"            .d$"       "$$.           ^$r
        dP            z$$"         ^*$e.          "b
       4$            e$P             "$$           "
                    J$F               $$
                    $$               .$F
                   4$"               $P"
                   $"               dP 
           ''')
        return weathericon
    elif weathicon=='Tornado':
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''
_____                     . '@(@@@@@@@)@. (@@) `  .   '
(_____(_[h,       .  @@'((@@@@@@@@@@@)@@@@@)@@@@@@@)@
 oo  oo  o        @@(@@@@@@@@@@))@@@@@@@@@@@@@@@@)@@` .
              @.((@@@@@@@)(@@@@@@@@@@@@@@))@\@@@@@@@@@)@@@  .
             (@@@@@@@@@@@@@@@@@@)@@@@@@@@@@@\\@@)@@@@@@@@)
            (@@@@@@@@)@@@@@@@@@@@@@(@@@@@@@@//@@@@@@@@@) `
      __o   .@(@@@@)##&&&&&(@@@@@@@@)::_=(@\\@@@@)@@ .   .'
       /\     @@`(@@)###&&&&&!!;;;;;;::-_=@@\\@)@`@.
     _/|     `    @@(@###&&&&!!;;;;;::-=_=@.@\\@@     '
    '  /     ,,  `  @.#####&&&!!;;;::=-_= .@  \\
       `    &@__,      ####&&&!!;;::=_-   _--_  `      
              " "       ###&&!!;;:-_=    `o--o'     ,,
   ( __E_     )           ##&&!;::_=               ~\/~----~ 
 ( /\%%<  j             ##&&!;:=        \|--m/        /|--w\ 
   /==\%<   <%\)        ##&&!:-       /\/----~              
   \||=|=<  <%%\  )    #&!;:-        ~''~ 
 ( /|I=\=<   <[]|   m #&!;=       
  ((       ) <==| ))  #&!-
          )      )     #&=         
    (           )        #&-           
     |=||=|===|         \\#/'            
 ^^^^          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           ''')
        return weathericon
    elif weathicon=='Mist' or weathicon=='Smoke' or weathicon=='Haze' or weathicon=='Dust' or weathicon=='Fog' or weathicon=='Sand' or weathicon=='Dust' or weathicon=='Ash' or weathicon=='Squall':
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⡤⢤⣴⣶⣶⣤⠄⠀⠀⠀⠀⠀
⠀⠠⢴⣾⣿⣿⡿⠟⠛⠛⠛⠛⠛⢛⣉⣩⣥⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢤⣤⣶⣶⣶⣶⣶⣶⣤⣤⣤⣴⣶⣶⣶⣦⣄⣠⣤⣤⣤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⣉⣉⣀⣻⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠉⠉⠁⠀
⠀⠀⠀⠀⣀⣤⣀⡀⠀⠈⠉⠉⠛⠛⠛⠛⢉⣉⣩⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠒⠿⣿⣿⣿⡿⠗⠀⠀⠀⠀⠶⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠆⠀⠀
⠀⠀⠀⠀⠀⠉⣀⣀⣤⣤⣴⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣯⣍⣁⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠙⠛⠛⠛⠛⢛⣻⣿⣿⣿⣿⣿⣷⣦⣤⣄⡀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣶⣤⣀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠟⠛⠉⠀⠀
⠀⠀⢀⣀⣠⣤⣤⣬⣽⣿⣿⣟⣉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢩⣭⣿⣿⣿⡉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⢴⣶⣾⣿⣿⣿⣿⣶⠤⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀
           ''')
        return weathericon
    else:
        weathericon=Table.grid(padding=2)
        weathericon.add_column(style='blue',justify='left')
        weathericon.add_column(no_wrap=True)
        weathericon.add_row('''
         snow delse
           ''')
        return weathericon
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
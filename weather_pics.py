from rich.table import Table


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
        weathericon.add_column(style='bright_yellow',justify='left')
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
        weathericon.add_column(style='bright_black',justify='left')
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
        weathericon.add_column(style='bright_white',justify='left')
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
        weathericon.add_column(style='bright_yellow',justify='left')
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
        weathericon.add_column(style='bright_black',justify='left')
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
        weathericon.add_column(style='bright_black',justify='left')
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
from pystyle import Anime, Center, Colors, Colorate, System, Cursor
from pywebcopy import save_webpage

import random
import string
import time
import os

watermark = '''██████╗ ██████╗ ██████╗ ███╗   ██╗
╚════██╗██╔══██╗╚════██╗████╗  ██║
 █████╔╝██║  ██║ █████╔╝██╔██╗ ██║
 ╚═══██╗██║  ██║ ╚═══██╗██║╚██╗██║
██████╔╝██████╔╝██████╔╝██║ ╚████║
╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝'''

System.Size(80, 20)

Cursor.HideCursor()
System.Title('\u200b                                                                         Press ENTER to continue')
Anime.Fade(Center.Center(watermark), Colors.purple_to_blue, Colorate.Vertical, interval=0.100, enter=True)

Cursor.ShowCursor()
System.Title('\u200b                                                                                       By 3D3N')

gray = '\033[38;2;150;150;150m'
light_gray = '\033[38;2;200;200;200m'
white = '\033[38;2;255;255;255m'
blurple = '\033[38;2;88;101;242m'
red = '\033[38;2;255;0;0m'
light_red = '\033[38;2;255;100;100m'
green = '\033[38;2;0;255;0m'
light_green = '\033[38;2;100;255;100m'

url = input(f'\n  {gray}[{white}?{gray}] {blurple}URL de la page {gray}-> {white}')

output = 'output-' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
start = time.time()

try:
    kwargs = {'bypass_robots': True, 'project_name': output}
    save_webpage(url, 'data/', **kwargs)
    
    end = time.time()
    delai = end - start
    
    print(f'\n  {gray}[{green}!{gray}] {light_green}Téléchargement réussi en {green}{round(delai, 2)}{light_green}ms avec le nom {green}{output}{light_gray}')
    
    error = False

except:
    print(f'\n  {gray}[{red}!{gray}] {light_red}URL Invalide{light_gray}')
    
    error = True

content = f'''\n  {gray}[{white}?{gray}] {blurple}URL de la page {gray}-> {white}{url}
\n  {gray}[{red}!{gray}] {light_red}URL Invalide{light_gray}''' if error \
else f'''\n  {gray}[{white}?{gray}] {blurple}URL de la page {gray}-> {white}{url}
\n  {gray}[{green}!{gray}] {light_green}Téléchargement réussi en {green}{round(delai, 2)}{light_green} ms avec le nom {green}{output}{light_gray}'''

Cursor.HideCursor()

for i in range(15):
    os.system('cls')
    print(content)
    print(f"\n  Fin dans {15-i}s")
    time.sleep(1)
from pyfiglet import Figlet
import webbrowser
import time

custom_fig = Figlet(font='isometric1')
print(custom_fig.renderText('Pie'))
custom_fig = Figlet(font='isometric3')
print(custom_fig.renderText('JERRY'))
#custom_fig = Figlet(font='alligator')
#print(custom_fig.renderText('FOR FREE LUCK'))

time.sleep(3)

url = "http://piejerry.000webhostapp.com/"
webbrowser.open(url , new=0, autoraise=True)

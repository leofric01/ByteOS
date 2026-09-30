import os
import datetime
from System_tools import show_help
from System_tools import show_about
from System_tools import date
from System_tools import clear_screen
from System_tools import shutdown
while True:
  command_part=input('Enter your command here...:')
  if command_part =='0': 
   print(' Im here to help you')
   show_help()
  elif command_part =='1':
    print(' its all about ')
    show_help()
  elif command_part =='2':
   print('its the date now! ...')
   date()
  elif command_part =='3':
    print('its your info screen....')
    clear_screen()
  elif command_part =='4':
    print('good bye mate ....')
    shutdown()


def show_help():
    print("""
=====================================================
                 BYTEOS COMMAND MENU                 
=====================================================

[ 🖥️ SYSTEM COMMANDS ]
  help       - Display this assistance menu
  about      - Display system version and overview
  clear      - Clear the terminal screen
  whoami     - Show current active user
  date       - Show current system date and time
  history    - Show previously executed commands
  shutdown   - Exit ByteOS simulator

[ 📁 FILE SYSTEM ]
  ls         - List files and directories
  mkdir      - Create a new directory
  touch      - Create a new empty file
  write      - Append text to a file
  read       - Display file contents
  cd         - Change current directory
  rm         - Remove a file or directory

[ 🛠️ UTILITIES & SECURITY ]
  calc       - Open mini calculator
  login      - Switch active user account

=====================================================
""")
import platform

def show_about():
 print(f"""
=====================================================
ByteOS - Version 1.0
System Information:
  • OS System : {platform.system()}
  • OS Release: {platform.release()}
  • Processor : {platform.processor()}
=====================================================
""")
import datetime

def date():
 now = datetime.datetime.now()
 print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

import os

def clear_screen():
    # لو النظام ويندوز ينفذ cls، غير كده ينفذ clear (مثل لينكس وماك)
    os.system('cls' if os.name == 'nt' else 'clear')
def shutdown():
    print("Shutting down ByteOS... Goodbye!")
    exit()  # أو تقدر تستخدم break جوه الـ loop
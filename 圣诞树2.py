import platform
import os
os_name = platform.uname()[0]
IS_WIN = os_name == 'Windows'
os.system('cls' if IS_WIN else 'clear')

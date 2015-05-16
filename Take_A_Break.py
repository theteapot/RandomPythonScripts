# The point of this program is to open a new browser window every hour to notify the user that is time to take a break.
# time.sleep takes an argument of seconds.

import time
import webbrowser

myArray = [r"https://www.youtube.com/watch?v=_TcB3SBDVGY", r"https://www.youtube.com/watch?v=lRe9UmpOWys", r"https://www.youtube.com/watch?v=jZoTLP8O1qg"]

def myFunction():
    for song in range(0, 3):
        time.sleep(60 * 60)
        webbrowser.open(myArray[song])
        print(myArray[song])

myFunction()

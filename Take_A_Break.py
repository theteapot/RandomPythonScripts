# The point of this program is to open a new browser window every hour to notify the user that is time to take a break.
# It will also open a web browser that will play specified song

import time
import webbrowser

songArray = ["https://www.youtube.com/watch?v=_TcB3SBDVGY", "https://www.youtube.com/watch?v=lRe9UmpOWys", "https://www.youtube.com/watch?v=jZoTLP8O1qg"]

def main():
    for song in songArray:
        time.sleep(60 * 60)
        webbrowser.open(song)
        print(song)

main()

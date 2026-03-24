from datetime import datetime
from zoneinfo import ZoneInfo
import time
import os

while True:
    os.system("clear")  # clears the terminal for a clean display

    ny = datetime.now(ZoneInfo("America/New_York"))
    bz = datetime.now(ZoneInfo("America/Belize"))
    la = datetime.now(ZoneInfo("America/Los_Angeles"))

    print("New York:", ny.strftime("%A %x — %R / %I:%M:%S %p"))
    print("Belize:   ", bz.strftime("%A %x — %R / %I:%M:%S %p"))
    print("LA:       ", la.strftime("%A %x — %R / %I:%M:%S %p"))

    time.sleep(1)  # update every second

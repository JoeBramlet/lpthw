from datetime import datetime
from zoneinfo import ZoneInfo

ny = datetime.now(ZoneInfo("America/New_York"))
bz = datetime.now(ZoneInfo("America/Belize"))
la = datetime.now(ZoneInfo("America/Los_Angeles"))

print("New York:", ny.strftime("%A %x — %R / %I:%M %p"))
print("Belize:   ", bz.strftime("%A %x — %R / %I:%M %p"))
print("LA:       ", la.strftime("%A %x — %R / %I:%M %p"))


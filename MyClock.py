from datetime import datetime
import pytz

# Timezones
ny_tz = pytz.timezone("America/New_York")
bz_tz = pytz.timezone("America/Belize")
la_tz = pytz.timezone("America/Los_Angeles")

# Current times
ny = datetime.now(ny_tz)
bz = datetime.now(bz_tz)
la = datetime.now(la_tz)

# Output
print("New York:", ny.strftime("%A %x — %R / %I:%M %p"))
print("Belize:   ", bz.strftime("%A %x — %R / %I:%M %p"))
print("LA:       ", la.strftime("%A %x — %R / %I:%M %p"))

# ex3ba.py - Joe's version of Exercise 3 (Numbers and Math)

# Basic system specs
solar_panels = 4
panel_output_watts = 50
battery_capacity_kwh = 1.5
boat_speed_mph = 3.2
lake_distance_miles = 7.8

# Calculations
total_solar_output = solar_panels * panel_output_watts
battery_capacity_wh = battery_capacity_kwh * 1000
time_to_cross_hours = lake_distance_miles / boat_speed_mph
energy_generated_wh = time_to_cross_hours * total_solar_output

print("Solar panels:", solar_panels)
print("Panel output (each):", panel_output_watts, "watts")
print("Total solar output:", total_solar_output, "watts")
print("Battery capacity:", battery_capacity_wh, "watt-hours")
print("Lake distance:", lake_distance_miles, "miles")
print("Boat speed:", boat_speed_mph, "mph")
print("Time to cross lake:", time_to_cross_hours, "hours")
print("Energy generated during crossing:", energy_generated_wh, "watt-hours")

"""
Exercise 3 — Joe’s Notes

What I’m exploring:
    - Playing with numbers and math in Python.
    - Seeing how variables and calculations behave when I change the inputs.
    - Using real-world values from my lake-mapping and solar-boat projects.

Why it matters:
    - Math is the backbone of every control system, battery model, and navigation loop.
    - If I can express the system in numbers, I can simulate it, automate it, or optimize it.
    - This is the first step toward building smarter tools for my autonomous rigs.

My alternate example:
    - Instead of cars and passengers, I used solar panels, battery capacity,
      boat speed, and lake distance.
    - These are the actual numbers I think about when planning a mapping run.

Reflections:
    - Python makes it easy to tweak values and instantly see the results.
    - This helps me understand the relationships between speed, distance,
      energy generation, and battery storage.
    - It already feels more useful than the original exercise because it
      connects directly to my real projects.
"""

# What You Should See
"""
Solar panels: 4
Panel output (each): 50 watts
Total solar output: 200 watts
Battery capacity: 1500.0 watt-hours
Lake distance: 7.8 miles
Boat speed: 3.2 mph
Time to cross lake: 2.4375 hours
Energy generated during crossing: 487.5 watt-hours
"""

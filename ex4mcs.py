#ex4mcs.py

boats = 2
battery_capacity_kwh = 1.5
solar_panels = 4
panel_output_watts = 50

total_solar_output = solar_panels * panel_output_watts
total_energy_wh = battery_capacity_kwh * 1000

print("Boats:", boats)
print("Solar output:", total_solar_output, "watts")
print("Battery storage:", total_energy_wh, "watt-hours")


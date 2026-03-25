# ex4ba.py — Enhanced Version with Structured Notes
# Joe's Alt Demo for LPTHW Exercise 4

# --- Code Section ---

# Basic boat + solar + battery variables
boats = 2
solar_panels = 4
panel_output_watts = 50
battery_capacity_kwh = 1.5

# Calculations
total_solar_output = solar_panels * panel_output_watts
battery_capacity_wh = battery_capacity_kwh * 1000
average_output_per_boat = total_solar_output / boats

# Output
print("Number of boats:", boats)
print("Solar panels:", solar_panels)
print("Panel output (each):", panel_output_watts, "watts")
print("Total solar output:", total_solar_output, "watts")
print("Battery capacity:", battery_capacity_wh, "watt-hours")
print("Average solar output per boat:", average_output_per_boat, "watts")


# --- Notes Section ---
print("""
Exercise 4 — Joe’s Notes (Enhanced Version)

Lesson Overview:
    - Understanding how variables work in the real world.
    - Seeing how numbers can represent real equipment and real constraints.

Why This Matters:
    - This code uses examples directly tied to my lake-mapping and solar-boat projects.
    - It makes the abstract idea of "variables" feel practical and intuitive.

What I Noticed:
    - Calculations can be written almost like plain English.
    - Variable names matter — they make the code readable.
    - Python replaces variable names with values automatically.

My Alternate Example:
    - I replaced the carpool example with solar boats, panels, and batteries.
    - This mirrors the structure of the original exercise but uses real-world values.

Reflections:
    - This feels more natural than the book example.
    - I’m starting to see how code can model real systems.
    - Curious how far I can push these alternate demos.
""")


# --- What You Should See ---
"""
Number of boats: 2
Solar panels: 4
Panel output (each): 50 watts
Total solar output: 200 watts
Battery capacity: 1500.0 watt-hours
Average solar output per boat: 100.0 watts
"""

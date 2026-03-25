my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair ='Brown'

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usakky %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {my_age + my_height + my_weight}.")

#alternate verison
# Joe_ex5 demo.py
lake_name = "Moss Lake"
kayak_length_ft = 12
battery_capacity_ah = 20
solar_panel_watts = 50

print(f"I like mapping {lake_name}.")
print(f"My layak is {kayak_length_ft} feet long.")
print(f"The battery holds {battery_capacity_ah} amp-hours.")
print(f"The solar panel provides {solar_panel_watts} watts of power.")
print(f"Together, that's enough for long mapping runs on {lake_name}.")



print("""
==========================
  Joe’s Exercise Notes
==========================

What I’m exploring:
    - How Python treats function calls (print is a function in Python 3)
    - How f-strings work and why the 'f' prefix matters
    - The role of spacing in function calls and why clean syntax matters

Why it matters:
    - Python 3 requires print() as a function, unlike Python 2's print statement
    - f-strings allow live evaluation inside { } and make output cleaner
    - Consistent syntax builds muscle memory and prevents subtle bugs later

My alternate example:
    - (Describe your custom version or experiment for this exercise)

Reflections:
    - The 'f' is a mode switch that turns a string into an evaluated expression
    - Spacing before parentheses is allowed but breaks visual consistency
    - Understanding Python 2 vs 3 differences clarifies why LPTHW teaches strict form
    - (Add anything else you noticed or want to revisit)
""")


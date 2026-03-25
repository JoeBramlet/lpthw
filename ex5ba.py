# ex5ba.py — Enhanced Version with Structured Notes

# --- Code Section ---
name = 'Joe'
age = 52
height = 70  # inches
weight = 200 # pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is the classic LPTHW trick
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print()  # spacer



# --- Notes Section ---
print("""
Exercise 1 - Joe’s Notes (Enhanced Version)

Lesson Overview:
    - Exercise 5 is about format strings — using variables inside strings. .
    - f‑strings — the modern Python 3 way to embed variables inside strings

    - Variable naming discipline

    - Basic arithmetic with variables

    - How to structure a script that prints a narrative
Why This Matters:
    - String are what people are able to read.

What I Noticed:
    - f-strings are much easier to read than all the symbols used in Python 2.


    they are a lot more human and natural. 
    - f-strings must start with the letter 'f' before the opening quote.

    - 
    - 

My Alternate Example:
    - (    - I added a structured notes section to reinforce the lesson.
    - I used my own variables (name, age, etc.) instead of the book’s.
    - I kept the narrative style but made it more personal.
)

Reflections:
    - (Anything that stood out, confused you, or made you curious)
""")

# --- What You Should See ---
"""
Let's talk about Joe.
He's 70 inches tall.
He's 200 pounds heavy.
Actually that's not too heavy.
He's got Brown eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 52, 70, and 200 I get 322.
"""

# ex6ba.py — Enhanced Version with Structured Notes

# --- Code Section ---
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


# --- Notes Section ---
print("""
Exercise 6 — Joe’s Notes

Lesson Overview:
    - Understanding how old-style % formatting works
    - How to embed values inside strings
    - How %d, %s, and %r behave differently
    - How variables can contain strings that get inserted into other strings
    - How string concatenation works (w + e)

What I’m exploring:
    - How % formatting inserts values into strings
    - The difference between %d, %s, and %r
    - How variables can contain strings that get inserted into other strings
    - Why w + e concatenates into one longer string

Why it matters:
    - String formatting is everywhere in real code
    - Understanding %r vs %s helps with debugging vs presentation
    - Concatenation is the foundation for building dynamic text

My alternate example:
    - (You’ll write a modern f-string version + a playful demo)

Reflections:
    - (Anything that surprised you, confused you, or clicked)
""")


# --- What You Should See ---
"""
There are 10 types of people.
Those who know binary and those who don't.
I said: 'There are 10 types of people.'.
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This is the left side of...a string with a right side.
"""

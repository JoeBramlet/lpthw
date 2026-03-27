
# ex7.py - Joe's LPTHW version

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
print("." * 10)  # prints 10 dots

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Notice the end=' ' to keep the next print on the same line
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# ...
# (your Exercise 5 code)
# ...


"""
==========================
 Joe’s Exercise 7 Notes
==========================

What I’m exploring:

1. String formatting
   "white as {}".format("snow")
   This shows how Python inserts values into strings. It’s the older
   formatting style, but understanding it helps me recognize legacy code.
   Later I’ll use f-strings, which are cleaner.

2. String repetition
   "." * 10
   Python repeats strings using the * operator. This is a simple example,
   but the concept becomes powerful for formatting, separators, and
   generating patterns.

3. Concatenation
   end1 + end2 + ...
   Building a word letter-by-letter. It’s intentionally tedious so I get
   a feel for how Python handles strings and how expressions combine.

4. Controlling print endings
   print(..., end=' ')
   Keeps the next print on the same line. In Python 2, a trailing comma
   did this. In Python 3, the comma no longer controls print behavior.
   Using end=' ' is the modern, explicit way.

Why it matters:
    - These tiny mechanics build muscle memory.
    - Understanding how Python handles strings prepares me for formatting,
      debugging, and building readable output later.
    - The print(end=' ') pattern shows up everywhere in real code.

My alternate example:
    - Maybe build a word like "Python Rocks" using letters, or repeat a
      pattern like "=" * 40 to create a header.

Reflections:
    - (Fill this in after running the script)
    - What surprised me?
    - What felt easy?
    - What clicked?
"""


import sys

# Take the values of a, b and c from the client.
a = int(input("What is the value of a? "))

if a == 0:       # Set a condition for a == 0
    print("No")
    sys.exit(1)

b = int(input("What is the value of b? "))
c = int(input("What is the value of c? "))

# Write the quadratic formulas for the two outcomes
D = b ** 2 - 4 * a * c
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

# Set the conditions of the "print" functions
if D == 0:
    print(f"The solution for {a}x²+{b}x+{c} is {x1:.2f}.")
elif D == 0 and b < 0:
    print(f"The solution for {a}x²{b}x+{c} is {x1:.2f}.")
elif D == 0 and c < 0:
    print(f"The solution for {a}x²+{b}x{c} is {x1:.2f}.")
elif D == 0 and c < 0 and b < 0:
    print(f"The solution for {a}x²{b}x{c} is {x1:.2f}.")
elif D == 0 and b == 0 and c == 0:
    print(f"The solution for {a}x² is zero.")

elif D < 0:
    print(f"I'm sorry, but for {a}x²+{b}x+{c} there is no real solution.")
elif D < 0 and b < 0:
    print(f"I'm sorry, but for {a}x²{b}x+{c} there is no real solution.")
elif D < 0  and c < 0:
    print(f"I'm sorry, but for {a}x²+{b}x{c} there is no real solution.")
elif D < 0 and b < 0 and c < 0:
    print(f"I'm sorry, but for {a}x²{b}x{c} there is no real solution.")
elif D < 0 and b == o:
    print(f"I'm sorry, but for {a}x²+{c} there is no real solution.")
elif D < 0 and b == 0 and c < 0 and a > 0:
    print(f"I'm sorry, but for {a}x²{c} there is no real solution.")

elif D > 0 and b < 0:
    print(f"The solutions for {a}x²{b}x+{c} are {x1:.2f} and {x2:.2f}")
elif D > 0 and c < 0:
    print(f"The solutions for {a}x²+{b}x{c} are {x1:.2f} and {x2:.2f}")
elif D > 0 and b < 0 and c < 0:
    print(f"The solutions for {a}x²{b}x{c} are {x1:.2f} and {x2:.2f}")
elif D > 0 and b == 0:
    print(f"The solutions for {a}x²+{c} are {x1:.2f} and {x2:.2f}")
elif D < 0 and b == 0 and c < 0:
    print(f"The solutions for {a}x²{c} are {x1:.2f} and {x2:.2f}")
elif D < 0 and c == 0:
    print(f"The solutions for {a}x²+{b}x are {x1:.2f} and {x2:.2f}")
elif D < 0 and c == 0 and b < b:
    print(f"The solutions for {a}x²{b}x are {x1:.2f} and {x2:.2f}")

print("     ")
print("Thank you very much for using the Quadratic Formula Calculator.")
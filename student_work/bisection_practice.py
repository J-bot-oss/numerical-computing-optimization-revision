# Practical Revision 01: Bisection Method

# Step 1: Define the function
def f(x):
    return x**3-x-2

# Step 2: Define the initial interval
a = 1
b = 2

# Step 3: Check the function at both endpoints
print("f(a) =", f(a))
print("f(b) =", f(b))

# Step 4: Calculate the midpoint
c = (a + b) /2

print("Midpoint =", c)
print("f(c) =", f(c))

# Step 5: Select the interval containing a root
if f(a) * f(c) < 0:
    b = c
elif f(c) * f(b) < 0:
    a = c
else:
    print("A root may have been found at the midpoint.")

print("New interval:", a, b)
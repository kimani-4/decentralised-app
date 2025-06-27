import numpy as np
from scipy.integrate import dblquad

# Define the function for the surface
def surface(x, y):
    return x**2 + y**2

# Define the limits for x and y
x_lower = 0
x_upper = 1
y_lower = 0
y_upper = 1

# Calculate the volume using double integration
volume, error = dblquad(surface, x_lower, x_upper, lambda x: y_lower, lambda x: y_upper)

# Print the result
print(f"The volume under the surface z = x^2 + y^2 over the region 0 ≤ x, y ≤ 1 is: {volume}")

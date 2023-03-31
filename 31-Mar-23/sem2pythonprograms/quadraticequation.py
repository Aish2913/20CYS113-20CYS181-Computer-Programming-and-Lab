# a is the coeficient of x^2
# b is the coeficient of x
# c is the constant value
# Root1 and Root2 are the roots of the Quadratic equation
print("Enter the coefficient of x^2")
a = int(input())
print("Enter the coefficient of x")
b = int(input())
print("Enter the constant value")
c = int(input())

# Root1 is
root1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# Root2 is
root2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print("One of the root of the given Quadratic Equation is" + str(root1))
print("Other root of the given Quadratic Equation is" + str(root2))
print("Thank you")

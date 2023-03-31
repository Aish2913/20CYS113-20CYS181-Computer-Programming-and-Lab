array = [0] * (n)
placeholder = [0] * (n)

print("enter the no of elements in an array")
n = int(input())
for counter in range(0, n - 1 + 1, 1):
    print("enter the elements")
    elements = int(input())
    array[counter] = elements
counter = 0
for counter in range(0, n - 1 + 1, 1):
    for counter in range(0, n - 1 - counter - 1 + 1, 1):
        # if Conditional:
            # pass

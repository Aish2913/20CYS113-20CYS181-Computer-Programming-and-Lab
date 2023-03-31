# Multiplication table
i = 1
n = 1
for i in range(1, 10 + 1, 1):
    print("The multiplication table of " + str(i) + " is")
    for n in range(1, 10 + 1, 1):
        print(str(i) + "*" + str(n) + "=" + str(n * i))

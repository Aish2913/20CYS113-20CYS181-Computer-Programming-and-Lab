def fibonacci(f):
    print("enter the number to find fibbonacci sequence")
    i = 0
    fv = 0
    sv = 1
    for i in range(0, f - 1 + 1, 1):
        if i < 1 or i == 1:
            n = i
        else:
            n = fv + sv
            fv = sv
            sv = n
        print(n)

# Main
print("enter the number to find fibbonacci sequence")
p = int(input())
fibonacci(p)

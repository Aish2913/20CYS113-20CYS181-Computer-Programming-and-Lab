# sum of n natural numbers
sum = 0
print("Enter the value of n")
n = int(input())
for i in range(1, n + 1, 1):
    
    # to calculate sum
    sum = sum + i
print("Sum of n natural numbers is" + str(sum))

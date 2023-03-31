inp = input()
length = len(inp)
count = 0
for i in range(0, length - 1 + 1, 1):
    ch = inp[i]
    for j in range(i + 1, length - 1 + 1, 1):
        ch1 = inp[j]
        if ch == ch1 and ch != " ":
            count = count + 1
if count == 0:
    print("heterogram")
else:
    print("not a heterogram")

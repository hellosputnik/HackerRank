L = input()
R = input()

result = 0

for a in range(L, R + 1):
    for b in range(L, R + 1):
        if a ^ b > result:
            result = (a ^ b)

print result


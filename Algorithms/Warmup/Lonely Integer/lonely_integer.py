N = input()
A = map(int, raw_input().split())

exclusive = 0

for a in A:
    exclusive ^= a
    
print exclusive


N, M = map(int, raw_input().split())

persons, teams, topics = [], 0, 0

for n in xrange(N):
    persons.append(raw_input())

for one in xrange(N):
    for two in xrange(one + 1, N):
        y = str(bin(int(persons[one], 2) | int(persons[two], 2))).count("1")
        if y > topics:
            teams, topics = 1, y
        elif y == topics:
            teams += 1

print "%s\n%s" % (topics, teams)


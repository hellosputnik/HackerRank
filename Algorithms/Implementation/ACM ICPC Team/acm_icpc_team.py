def calculate(N, people):
    teams, topics = 0, 0

    for left in xrange(N):
        for right in xrange(left + 1, N):
            combo = str(bin(int(people[left], 2) | int(people[right], 2))).count("1")
            if combo > topics:
                teams, topics = 1, combo
            elif combo == topics:
                teams += 1

    return ("%s\n%s" % (topics, teams))
 
def main():
    N, M = map(int, raw_input().split())
    
    people = []
    
    for n in xrange(N):
        people.append(raw_input())
    
    print calculate(N, people)

if __name__ == '__main__':
    main()


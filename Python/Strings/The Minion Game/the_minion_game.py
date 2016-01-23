import collections

def main():
    S = raw_input()

    scores = collections.defaultdict(int)
    
    length = len(S)
    for index in xrange(length):
        if S[index] in "AEIOU":
            scores["K"] += (length - index)
        else:
            scores["S"] += (length - index)

    if scores["K"] > scores["S"]:
        print "Kevin", scores["K"]
    if scores["K"] < scores["S"]:
        print "Stuart", scores["S"]

    if scores["K"] == scores["S"]:
        print "Draw"

if __name__ == '__main__':
    main()


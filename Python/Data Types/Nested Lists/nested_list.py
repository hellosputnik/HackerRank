from __future__ import print_function

import collections

def main():
    N = input()

    S = collections.OrderedDict()
    for n in xrange(N):
        name, marks = raw_input(), input()
        S[name] = marks

    value = sorted(set(S.values()))[1]
    map(print, sorted([s[0] for s in S.items() if s[1] == value]))

if __name__ == '__main__':
    main()


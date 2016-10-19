import collections
import re

N, M = map(int, raw_input().split())

message = collections.defaultdict(str)
for n in xrange(N):
    line = raw_input()
    for index, character in enumerate(line):
        message[index] += character

print re.sub(r"\b[^\w]+\b", " ", "".join(message.values()).strip())


import re

P = raw_input()

print bool(re.search("^[\d]{6}$", P) and not re.search(r"(.)(.)\1\2", P))

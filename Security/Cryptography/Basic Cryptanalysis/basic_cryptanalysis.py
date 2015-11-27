encryption = {}

encryption["a"] = "w"
encryption["b"] = "z"
encryption["c"] = "t"
encryption["d"] = "b"
encryption["e"] = "e"
encryption["f"] = "a"
encryption["g"] = "c"
encryption["h"] = "k"
encryption["i"] = "i"
encryption["j"] = "o"
encryption["k"] = "w"
encryption["l"] = "s"
encryption["m"] = "p"
encryption["n"] = "v"
encryption["o"] = "l"
encryption["p"] = "u"
encryption["q"] = "g"
encryption["r"] = "d"
encryption["s"] = "r"
encryption["t"] = "i"
encryption["u"] = "w"
encryption["v"] = "h"
encryption["w"] = "f"
encryption["x"] = "y"
encryption["y"] = "n"
encryption["z"] = "m"

ciphertext = list(raw_input())

for i, c in enumerate(ciphertext):
    if c in encryption:
        ciphertext[i] = encryption[c]
    else:
        continue

print ''.join(ciphertext)


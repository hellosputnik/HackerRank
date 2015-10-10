import collections

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decipher(ciphertext, keyword):
    plaintext = ""
    
    key = "".join(collections.OrderedDict.fromkeys(keyword))
    alphabet = key[:]

    for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if character not in key:
            alphabet += character

    substitution = ""
    for k in sorted(key):
        substitution += "".join([alphabet[i] for i in xrange(alphabet.index(k), len(alphabet), len(key))])

    for character in ciphertext:
        if character == " ":
            plaintext += " "
            continue
        plaintext += ALPHABET[substitution.index(character)]

    return plaintext

def main():
    N = input()

    for n in xrange(N):
        keyword, ciphertext = raw_input(), raw_input()

        print decipher(ciphertext, keyword)

if __name__ == '__main__':
    main()


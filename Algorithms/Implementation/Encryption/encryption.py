import math

def encrypt(text, key):
    text = text.replace(" ", "")
    ciphertext = ""

    for i in xrange(key):
        ciphertext += ''.join(text[i::key]) + " "

    return ciphertext

def main():
    plaintext = raw_input()

    key = int(math.ceil(math.sqrt(len(plaintext))))
    print encrypt(plaintext, key)

if __name__ == '__main__':
    main()


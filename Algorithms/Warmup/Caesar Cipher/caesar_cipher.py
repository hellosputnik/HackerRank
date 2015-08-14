def encrypt(string, key):
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

    ciphertext = str()
    for char in string:
        if char.isalpha():
            ciphertext += alphabet[(alphabet.index(char) + (2 * key)) % 52]
        else:
            ciphertext += char

    return ciphertext

def main():
    N = input()
    S = raw_input()
    K = input()

    print encrypt(S, K)

if __name__ == '__main__':
    main()


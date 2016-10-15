import collections
import itertools
import operator


# Reverse the substitution on the string using the dctionary as a map.
def decrypt(string, dictionary):

    buf = list(string)

    seen = []
    for char in string:
        for index in [i for i, letter in enumerate(string) if letter == char]:
            if index not in seen and char in dictionary:
                seen.append(index)
                buf[index] = dictionary[char]

    return "".join(buf)


# Using the remaining keys and values, brute force the remaining combinations.
def correct(errors, unused_keys, unused_values, plaintext):
    replacements = collections.defaultdict(str)

    for error in errors:
        for char in error:
            if char not in unused_keys:
                continue
            indices = [index for index, c in enumerate(error) if char == c]
            for value in unused_values:
                for combo in combine(indices):
                    replacement = list(error)
                    for index in combo:
                        replacement[index] = value
                    replacement = "".join(replacement)
                    if replacement in plaintext:
                        replacements[error] = replacement
                        break

    return replacements


# Create all possible combinations of replacement indices.
def combine(indices):
    combinations = []

    for size in xrange(1, len(indices) + 1):
        # Creates combinations according to the size, which ranges from 1 to
        # the number of indices.
        combinations.extend(list(itertools.combinations(indices, size)))

    return combinations

# Reduce/simplify the string to an easily isomorphic-identifiable format.
def simplify(word):
    """
    Replace each character with a unique symbol; in this case, numbers are
    used as symbols, which limits strings to 10 unique characters (i.e. 0-9).
    """
    strbuf = word[:]

    counter = 0
    seen = []
    for letter in word:
        if letter not in seen:
            seen.append(letter)
            strbuf = strbuf.replace(letter, str(counter))
            counter += 1

    return strbuf


def main():

    # Read the ciphertext from stdin
    ciphertext = raw_input().split()

    # Read the dictionary/plaintext from file
    with open("dictionary.lst", 'r') as f:
        plaintext = f.read().lower().split()

    # Construct a dictionary of words and its character uniqueness sorted by
    # words with least uniqueness/high redundancy first. Those words are the
    # high value words that will enable effective analysis.
    redundancy = {}
    for word in plaintext:
        redundant = len(word) - len(set(word))
        if redundant:
            redundancy[word] = redundant
    redundancy = sorted(redundancy.items(), key=operator.itemgetter(1), reverse=True)

    # Develop a substitution map starting with the words with the highest
    # redundancy.
    key = collections.defaultdict(list)
    for word in redundancy:
        simplified = simplify(word[0])
        for text in ciphertext:
            if simplified == simplify(text):
                for index, letter in enumerate(word[0]):
                    # Do not replace previous mappings from higher valued
                    # analysis
                    key[text[index]].extend([letter] * (word[1] * 2))

    for item in key:
        key[item] = collections.Counter(key[item]).most_common(5)

    key = sorted(key.items(), key=lambda x: x[1][0][1], reverse=True)
    seen = []
    table = {}
    for item in key:
        for i in xrange(len(item[1])):
            if item[1][i][0] not in seen:
                seen.append(item[1][i][0])
                table[item[0]] = item[1][i][0]
                break


    buf, errors = [], []
    for text in ciphertext:
        result = decrypt(text, table)
        if result not in plaintext:
            errors.append(result)
        buf.append(result)

    unused_keys = set("abcdefghijklmnopqrstuvwxyz") - set(table.keys())
    unused_values = set("abcdefghijklmnopqrstuvwxyz") - set(seen)
    corrections = correct(errors, unused_keys, unused_values, plaintext)
    for index, word in enumerate(buf):
        if word in corrections:
            buf[index] = corrections[word]

    print " ".join(buf)

if __name__ == '__main__':
    main()


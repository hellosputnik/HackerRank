#!/usr/bin/env python


def _is_vowel(char):
    return char in "aeiouy"


def score(word):
    vowels = filter(_is_vowel, word)
    return 2 if len(vowels) % 2 == 0 else 1


def score_words(words):
    return sum(map(score, words))


"""
def main():
    n     = input()
    words = raw_input().split()

    print sum(map(score, words))


if __name__ == '__main__':
    main()
"""


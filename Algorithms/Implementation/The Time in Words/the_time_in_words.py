def convert(H, M):
    WORDS = [
        'null', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 
        'twenty'
        ]

    hours = WORDS[H % 12] if M <= 30 else WORDS[(H + 1) % 12]

    if M == 0:
        minutes = " o' clock"
        return (hours + minutes)
    if M == 1:
        minutes = "one minute past "
        return (minutes + hours)
    if M == 15:
        minutes = "quarter past "
        return (minutes + hours)
    if M == 30:
        minutes = "half past "
        return (minutes  + hours)
    if M == 45:
        minutes = "quarter to "
        return (minutes + hours)

    if M < 30:
        if M < 20:
            minutes = WORDS[M] + " minutes past "
        else:
            minutes = "twenty " + WORDS[(M - 20)] + " minutes past "
    else:
        M = 60 - M
        if M < 20:
            minutes = WORDS[M] + " minutes to "
        else:
            minutes = "twenty " + WORDS[(M - 20)] + " minutes to "

    return (minutes + hours)

def main():
    H = input()
    M = input()

    print convert(H, M)

if __name__ == '__main__':
    main()


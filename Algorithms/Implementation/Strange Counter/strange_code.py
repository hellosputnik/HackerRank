def generate():
    lower, upper = 1, 3

    counter = 6
    while True:
        yield (lower, upper)
        lower = lower * 2 + 2
        upper += counter
        counter *= 2


def f(t):
    for index, counter in enumerate(generate()):
        if t >= counter[0] and t <= counter[1]:
            return (3 * 2 ** index) - (t - counter[0])


def main():
    t = input()

    print f(t)


if __name__ == '__main__':
    main()


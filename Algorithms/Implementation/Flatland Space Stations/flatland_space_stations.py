def main():
    n, m = map(int, raw_input().split())
    stations = sorted(map(int, raw_input().split()))

    maximum_distance = max(stations[0], ((n - 1) - stations[-1]))
    for i in xrange(m - 1):
        distance = abs(stations[i] - ((stations[i + 1] + stations[i]) / 2))
        if distance > maximum_distance:
            maximum_distance = distance

    print maximum_distance


if __name__ == '__main__':
    main()


import math

def main():
    AB, BC = (float(input()) for _ in xrange(2))

    print "%d°" % round(math.degrees(math.atan(AB/BC)))

if __name__ == '__main__':
    main()


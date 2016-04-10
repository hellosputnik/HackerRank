import math

class Complex:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __add__(self, other):
        return Complex(self.A + other.A, self.B + other.B)

    def __sub__(self, other):
        return Complex(self.A - other.A, self.B - other.B)

    def __mul__(self, other):
        R = self.A * other.A - self.B * other.B
        I = self.A * other.B + self.B * other.A
        return Complex(R, I)

    def __div__(self, other):
        R = (self.A * other.A + self.B * other.B) / (other.A ** 2 + other.B ** 2)
        I = (self.B * other.A - self.A * other.B) / (other.A ** 2 + other.B ** 2)
        return Complex(R, I)

    def __abs__(self):
        return "%.2f+0.00i" % math.sqrt(self.A ** 2 + self.B ** 2)

    def __str__(self):
        return '{0:.2f}{1:+.2f}i'.format(self.A, self.B)

def main():
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())

    C = Complex(c[0], c[1])
    D = Complex(d[0], d[1])

    print '\n'.join(map(str, [C + D, C - D, C * D, C / D, abs(C), abs(D)]))

if __name__ == '__main__':
    main()


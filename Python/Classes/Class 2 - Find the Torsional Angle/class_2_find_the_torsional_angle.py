import math

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def dot(a, b):
    return sum([a[x]*b[x] for x in range(3)])

def norm(a):
    return sum([a[x]**2 for x in range(3)])**0.5

def main():

    a, b, c, d = ([map(float, raw_input().split()) for _ in xrange(4)])

    ab = list([b[x]-a[x] for x in range(3)])
    bc = list([c[x]-b[x] for x in range(3)])
    cd = list([d[x]-c[x] for x in range(3)])

    abc = cross(ab, bc)
    bcd = cross(bc, cd)

    print '{0:.2f}'.format(math.degrees(math.acos(dot(abc,bcd)/(norm(abc)*norm(bcd)))))

if __name__ == '__main__':
    main()


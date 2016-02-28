import collections

def main():
    N = input()
    columns = raw_input().split()

    Student = collections.namedtuple('Student', " ".join(columns))

    students = []
    for n in xrange(N):
        column = raw_input().split()
        student = Student(column[0], column[1], column[2], column[3]) 
        
        students.append(student)

    average = 0.0
    for student in students:
        average += float(student.MARKS)

    print average / N

if __name__ == '__main__':
    main()


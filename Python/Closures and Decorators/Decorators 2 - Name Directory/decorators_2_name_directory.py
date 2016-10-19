import operator

def formatter(func):
    def format(data):
        def transform(gender):
            return "Mr. " if gender == 'M' else "Ms. "
        formated_data = [(transform(entry[3]) + entry[0] + " " + entry[1], entry[2]) for entry in data]
        return func(formated_data, key=operator.itemgetter(1))
    return format

def main():
    N = input()

    persons = []
    for n in xrange(N):
        person = raw_input().split()
        persons.append(person)

    formated_sort = formatter(sorted)

    for person in formated_sort(persons):
        print person[0]


if __name__ == '__main__':
    main()


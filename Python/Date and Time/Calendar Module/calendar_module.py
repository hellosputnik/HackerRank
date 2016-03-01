import calendar

def main():
    MM, DD, YYYY = map(int, raw_input().split())

    weekday = calendar.weekday(YYYY, MM, DD)

    if weekday == 0:
        print "MONDAY"
    if weekday == 1:
        print "TUESDAY"
    if weekday == 2:
        print "WEDNESDAY"
    if weekday == 3:
        print "THURSDAY"
    if weekday == 4:
        print "FRIDAY"
    if weekday == 5:
        print "SATURDAY"
    if weekday == 6:
        print "SUNDAY"

if __name__ == '__main__':
    main()


def main():
    time = raw_input()

    hh = time[0:2]
    mm = time[3:5]
    ss = time[6:8]
    
    period = time[8:10]

    if hh != "12" and period == "PM":
        hh = str(int(hh) + 12)
    elif hh == "12" and period == "AM":
        hh = "00"

    print hh + ":" + mm + ":" + ss

if __name__ == '__main__':
    main()


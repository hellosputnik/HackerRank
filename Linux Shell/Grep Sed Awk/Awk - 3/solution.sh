awk '{
    average = (($2 + $3 + $4) / 3);
    printf "%s : ", $0;
    if(average >= 80)
        print "A";
    else if(average >= 60)
        print "B";
    else if(average >= 50)
        print "C";
    else
        print "FAIL";
}'

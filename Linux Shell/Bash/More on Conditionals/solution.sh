read X
read Y
read Z

if [ $X -eq $Y ]
then
    if [ $Y -eq $Z ]
    then
        echo "EQUILATERAL"
    else
        echo "ISOSCELES"
    fi
else
    if [ $Y -eq $Z ]
    then
        echo "ISOSCELES"
    else
        echo "SCALENE"
    fi
fi


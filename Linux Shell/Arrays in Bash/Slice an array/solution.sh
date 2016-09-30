while read line
do
    names=("${names[@]}" $line);
done

echo ${names[@]:3:5}

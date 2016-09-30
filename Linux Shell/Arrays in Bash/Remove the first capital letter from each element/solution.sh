while read line
do
    names=("${names[@]}" $line);
done

echo ${names[@]/[A-Z]/.}

read N

for ((n = 1; n <= N; ++n));
{
	read x;
	sum=$((sum + x));
}

printf "%.3f" $(echo "scale=4;$sum/$N" | bc)


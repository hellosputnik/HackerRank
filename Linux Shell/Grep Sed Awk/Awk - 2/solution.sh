awk '{ printf $1 " : "; if($2 >= 50 && $3 >= 50 && $4 >= 50) print "Pass"; else print "Fail"; }';

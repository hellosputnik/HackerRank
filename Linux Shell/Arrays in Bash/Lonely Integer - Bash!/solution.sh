read N;

A=$(cat)
A=${A[*]};

echo $((${A// /^}));

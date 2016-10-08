factorial = -> (n) { (1..n).reduce(:*) || 1 }

combination = -> (n) do
    -> (r) do
        factorial.call(n) / (factorial.call(r) * factorial.call(n - r))
    end
end

n = gets.to_i
r = gets.to_i
nCr = combination.(n)
puts nCr.(r)


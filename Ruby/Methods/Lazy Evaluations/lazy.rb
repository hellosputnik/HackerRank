require 'prime'

N = gets.to_i

array = Prime.each.lazy.select do |p|
    p.to_s == p.to_s.reverse
end.first(N)

print array


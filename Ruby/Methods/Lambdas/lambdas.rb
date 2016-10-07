square      = lambda { |integer| return integer ** 2; }

plus_one    = lambda { |integer| return integer + 1; }

into_2      = lambda { |integer| return integer * 2; }

adder       = lambda { |x, y| return x + y; }

values_only = lambda { |hash| return hash.values(); }


input_number_1 = gets.to_i
input_number_2 = gets.to_i
input_hash = eval(gets)

a = square.(input_number_1); b = plus_one.(input_number_2);c = into_2.(input_number_1);
d = adder.(input_number_1, input_number_2);e = values_only.(input_hash)

p a; p b; p c; p d; p e


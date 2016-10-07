def factorial
    yield;
end

n = gets.to_i();

factorial do
    result = (1..n).reduce() { |product, multiplier| product *= multiplier };
    puts result;
end

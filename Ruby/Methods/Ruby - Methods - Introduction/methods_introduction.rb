def prime?(number)
    if number < 2
        return false;
    elsif number == 2 or number == 3
        return true;
    else
        return (2..(number/2)).all? { |divisor| number % divisor != 0; };
    end
end

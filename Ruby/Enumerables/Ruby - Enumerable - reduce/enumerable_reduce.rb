def sum_terms(n)
    return (0..n).reduce() { |sum, item| sum += (item**2 + 1) };
end


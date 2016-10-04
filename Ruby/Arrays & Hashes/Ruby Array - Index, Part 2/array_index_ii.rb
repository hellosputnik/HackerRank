def neg_pos(array, index)
    return array[-index];
end

def first_element(array)
    # array.first;
    return array[0];
end

def last_element(array)
    # array.last;
    return array[-1];
end

def first_n(array, n)
    # array.take(n);
    return array[0...n];
end

def drop_n(array, n)
    # array.drop(n);
    return array[n..-1];
end

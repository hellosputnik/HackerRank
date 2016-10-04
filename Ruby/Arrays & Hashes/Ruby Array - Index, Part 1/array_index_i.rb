def element_at(array, index)
    return array[index];
end

def inclusive_range(array, _start, _end)
    return array[_start.._end];
end

def non_inclusive_range(array, _start, _end)
    return array[_start..._end];
end

def start_and_length(array, start, length)
    return array[start..(start + length - 1)];
end

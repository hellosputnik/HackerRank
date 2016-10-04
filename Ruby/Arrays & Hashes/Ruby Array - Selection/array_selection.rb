def select_arr(array)
    return array.select { |a| a % 2 != 0 };
end

def reject_arr(array)
    return array.reject { |b| b % 3 == 0 };
end

def delete_arr(array)
    return array.delete_if { |c| c < 0 };
end

def keep_arr(array)
    return array.keep_if { |d| d >= 0 };
end

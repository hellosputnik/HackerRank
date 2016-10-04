def end_arr_add(array, element)
    array.push(element);
end

def begin_arr_add(array, element)
    array.unshift(element);
end

def index_arr_add(array, index, element)
    array.insert(index, element);
end

def index_arr_multiple_add(array, index)
    array.insert(index, 1, 2);
end

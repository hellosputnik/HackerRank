def func_any(hash)
    return hash.any? { |key, value| key.is_a?(Integer); }
end

def func_all(hash)
    return hash.all? { |key, value| value.is_a?(Integer) and value < 10; }
end

def func_none(hash)
    return hash.none? { |key, value| value.nil?(); }
end

def func_find(hash)
    return hash.find { |key, value|
        (key.is_a?(Integer) and value.is_a?(Integer) and value < 20) or
        (key.is_a?(String)  and value.is_a?(String)  and value.start_with?("a"));
    }
end


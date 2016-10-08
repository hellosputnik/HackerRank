def mask_article(string, array)
    array.each do |word|
        string.gsub!(word, strike(word))
    end
    return string
end

def strike(string)
    return "<strike>" + string + "</strike>"
end

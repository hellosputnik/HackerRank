def skip_animals(animals, skip)
    array = Array.new();
    animals.each_with_index do |item, index|
        array.push("#{index}:#{item}") unless index < skip;
    end
    return array;
end


def serial_average(string)
    x = string[4..8].to_f
    y = string[10..-1].to_f
    z = ((x + y) / 2).round(2)

    return "#{string[0..2]}-#{z}"
end

power_function = -> (x, z) {
    (x) ** z
}

base = gets.to_i
raise_to_power = -> (z) { power_function.call(base, z) }

power = gets.to_i
puts raise_to_power.(power)


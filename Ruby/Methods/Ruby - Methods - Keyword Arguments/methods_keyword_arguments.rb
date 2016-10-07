def convert_temp(temperature, input_scale: "undefined", output_scale: "undefined")
    case input_scale
    when "celsius"
        case output_scale
        when "fahrenheit"
            return ((temperature * (9 / 5.0)) + 32);
        when "kelvin"
            return (temperature + 273.15);
        end
    when "fahrenheit"
        case output_scale
        when "celsius"
            return ((temperature - 32) * (5.0 / 9.0));
        when "kelvin"
            return ((temperature - 32) * 5.0 / 9.0 + 273.15);
        end
    when "kelvin"
        case output_scale
        when "celsius"
            return (temperature - 273.15);
        when "fahrenheit"
            return (temperature * 5.0 / 9.0 + 32 + 273.15);
        end
    when "undefined"
        puts "Please specify a proper temperature unit.";
    end
end

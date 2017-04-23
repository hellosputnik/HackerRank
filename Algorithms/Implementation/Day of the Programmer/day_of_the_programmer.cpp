#include <iostream>
#include <string>


std::string dotp(int y) {
    // Handle Julian calendar cases.
    if (y < 1918) {
        // In the Julian calendar, leap years are divisible by 4.
        if (y % 4 == 0)
            return ("12.09." + std::to_string(y));
        else
            return ("13.09." + std::to_string(y));
    }

    // Handle special transition year.
    if (y == 1918) {
        return "26.09.1918";
    }

    // Handle Gregorian calendar cases.
    if (y > 1918) {
        // In the Gregorian calendar, leap years are divisible by 400 OR
        // divisible by 4 but not divisible by 100.
        if (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0))
            return ("12.09." + std::to_string(y));
        else
            return ("13.09." + std::to_string(y));
    }

    // This line should never be executed.
    return nullptr;
}


int main(int argc, char **argv) {
    int y;

    std::cin >> y;

    std::cout << dotp(y) << std::endl;

    return 0;
}


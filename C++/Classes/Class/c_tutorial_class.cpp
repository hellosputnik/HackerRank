#include <iostream>
#include <string>

#include "Student.h"

int main(int argc, char **argv)
{
    Student s;

    int age;
    std::string first_name, last_name;
    int standard;

    std::cin >> age >> first_name >> last_name >> standard;

    s.set_age(age);
    s.set_first_name(first_name);
    s.set_last_name(last_name);
    s.set_standard(standard);

    std::cout << s.get_age() << std::endl;
    std::cout << s.get_last_name() << ", " << s.get_first_name() << std::endl;
    std::cout << s.get_standard() << '\n' << std::endl;

    std::cout << s.to_string() << std::endl;

    return 0;
}


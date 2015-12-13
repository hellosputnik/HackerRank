#include <iostream>
#include <string>

struct Student
{
    int age;
    std::string first_name;
    std::string last_name;
    int standard;
};

int main(int argc, char **argv)
{
    Student s;

    std::cin >> s.age >> s.first_name >> s.last_name >> s.standard;

    std::cout << s.age << " ";
    std::cout << s.first_name << " ";
    std::cout << s.last_name << " ";
    std::cout << s.standard << " ";

    return 0;
}


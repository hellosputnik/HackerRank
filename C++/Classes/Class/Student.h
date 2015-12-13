#include <sstream>
#include <string>

class Student
{

private:

    int age;
    std::string first_name;
    std::string last_name;
    int standard;

public:

    void set_age(int age);
    void set_first_name(std::string first_name);
    void set_last_name(std::string last_name);
    void set_standard(int standard);

    int get_age();
    std::string get_first_name();
    std::string get_last_name();
    int get_standard();

    std::string to_string();
};

void Student::set_age(int age)
{
    this->age = age;
}

void Student::set_first_name(std::string first_name)
{
    this->first_name = first_name;
}

void Student::set_last_name(std::string last_name)
{
    this->last_name = last_name;
}

void Student::set_standard(int standard)
{
    this->standard = standard;
}

int Student::get_age()
{
    return age;
}

std::string Student::get_first_name()
{
    return first_name;
}

std::string Student::get_last_name()
{
    return last_name;
}

int Student::get_standard()
{
    return standard;
}

std::string Student::to_string()
{
    std::stringstream sstream;

    sstream << age << ",";
    sstream << first_name << ",";
    sstream << last_name << ",";
    sstream << standard;

    return sstream.str();
}


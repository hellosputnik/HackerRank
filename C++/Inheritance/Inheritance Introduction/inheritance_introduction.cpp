#include <iostream>

class Triangle
{

public:

    void triangle() { std::cout << "I am a triangle\n"; }

};

class Isosceles : public Triangle
{

public:

    void description() { std::cout << "In an isosceles triangle two sides are equal\n"; }
    void isosceles() { std::cout << "I am an isosceles triangle\n"; }

};

int main(int argc, char **argv)
{
    Isosceles i;

    i.isosceles();
    i.description();
    i.triangle();

    return 0;
}


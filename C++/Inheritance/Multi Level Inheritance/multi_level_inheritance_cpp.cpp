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

class Equilateral : public Isosceles
{

public:

    void equilateral() { std::cout << "I am an equilateral triangle\n"; }

};

int main(int argc, char **argv)
{
    Equilateral e;

    e.equilateral();
    e.isosceles();
    e.triangle();

    return 0;
}


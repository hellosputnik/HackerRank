#include <cstdlib>
#include <iostream>

int add(int *a, int *b)
{
    return (*a + *b);
}

int difference(int *a, int *b)
{
    return abs(*a - *b);
}

int main(int argc, char **argv)
{
    int a, b;

    std::cin >> a >> b;

    std::cout << add(&a, &b) << std::endl;
    std::cout << difference(&a, &b) << std::endl;

    return 0;
}


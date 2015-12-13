#include <iostream>

void print(int n)
{
    switch(n)
    {
        case 1:
            std::cout << "one";
            break;
        case 2:
            std::cout << "two";
            break;
        case 3:
            std::cout << "three";
            break;
        case 4:
            std::cout << "four";
            break;
        case 5:
            std::cout << "five";
            break;
        case 6:
            std::cout << "six";
            break;
        case 7:
            std::cout << "seven";
            break;
        case 8:
            std::cout << "eight";
            break;
        case 9:
            std::cout << "nine";
            break;
        default:
            std::cout << (!(n % 2) ? "even" : "odd");
            break;
    }
    std::cout << std::endl;
}

int main(int argc, char **argv)
{
    int a, b;

    std::cin >> a >> b;

    for(int x = a; x <= b; ++x)
        print(x);

    return 0;
}


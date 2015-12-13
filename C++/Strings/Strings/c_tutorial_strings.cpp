#include <iostream>
#include <string>

int main(int argc, char **argv)
{
    std::string a, b;

    std::cin >> a >> b;

    std::cout << a.length() << " " << b.length() << std::endl;
    std::cout << a + b << std::endl;
    std::cout << b[0] << a.substr(1) << " " << a[0] << b.substr(1) << std::endl;

    return 0;
}


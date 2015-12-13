#include <iostream>
#include <sstream>

int main(int argc, char **argv)
{
    std::string buffer;

    getline(std::cin, buffer);
    std::stringstream sstream(buffer);

    std::string n;
    while(getline(sstream, n, ','))
        std::cout << n << std::endl;

    return 0;
}


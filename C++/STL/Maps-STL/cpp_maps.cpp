#include <iostream>
#include <map>
#include <string>

int main(int argc, char **argv)
{
    int Q;
    int type;
    std::string X;
    int Y;
    std::map<std::string, int> m;

    std::cin >> Q;

    for(int q = 0; q < Q; ++q)
    {
        std::cin >> type;

        switch(type)
        {
            case 1:
                std::cin >> X >> Y;
                m[X] += Y;
                break;
            case 2:
                std::cin >> X;
                m.erase(X);
                break;
            case 3:
                std::cin >> X;
                if(m.count(X))
                    std::cout << m[X] << std::endl;
                else
                    std::cout << 0 << std::endl;
                break;
        }
    }

    return 0;
}


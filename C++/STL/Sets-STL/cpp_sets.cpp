#include <algorithm>
#include <iostream>
#include <set>

int main(int argc, char **argv)
{
    int Q;
    int y, x;
    std::set<int> s;

    std::cin >> Q;

    for(int q = 0; q < Q; ++q)
    {
        std::cin >> y >> x;

        switch(y)
        {
            case 1:
                s.insert(x);
                break;
            case 2:
                s.erase(x);
                break;
            case 3:
                if(s.count(x))
                    std::cout << "Yes" << std::endl;
                else
                    std::cout << "No" << std::endl;
                break;
        }
    }

    return 0;
}


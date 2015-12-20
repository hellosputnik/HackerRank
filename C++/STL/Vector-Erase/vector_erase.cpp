#include <iostream>
#include <vector>

int main(int argc, char **argv)
{
    int N;
    std::vector<int> integers;
    int x;
    int a, b;

    std::cin >> N;

    int i;
    for(int n = 0; n < N; ++n)
    {
        std::cin >> i;
        integers.push_back(i);
    }

    std::cin >> x >> a >> b;

    integers.erase(integers.begin() + x - 1);
    integers.erase(integers.begin() + a - 1, integers.begin() + b - 1);

    std::cout << integers.size() << std::endl;
    for(auto it = integers.begin(); it != integers.end(); ++it)
        std::cout << *it << " ";
    std::cout << std::endl;

    return 0;
}


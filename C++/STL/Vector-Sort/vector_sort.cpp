#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char **argv)
{
    int N;
    std::vector<int> V;

    std::cin >> N;

    int i;
    for(int n = 0; n < N; ++n)
    {
        std::cin >> i;
        V.push_back(i);
    }

    std::sort(V.begin(), V.end());
    for(auto it = V.begin(); it != V.end(); ++it)
        std::cout << *it << " ";

    return 0;
}


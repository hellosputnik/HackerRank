#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char **argv)
{
    int N;
    std::vector<int> X;
    int Q;
    int Y;

    std::cin >> N;

    int i;
    for(int n = 0; n < N; ++n)
    {
        std::cin >> i;
        X.push_back(i);
    }

    std::cin >> Q;
    for(int q = 0; q < Q; ++q)
    {
        std::cin >> Y;

        auto it = lower_bound(X.begin(), X.end(), Y);
        if(*it == Y)
            std::cout << "Yes ";
        else
            std::cout << "No ";
        std::cout << it - X.begin() + 1 << std::endl;
    }

    return 0;
}


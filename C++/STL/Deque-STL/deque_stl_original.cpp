#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

int main(int argc, char **argv)
{
    int T;
    int N, K;
    std::deque<int> d;

    std::cin >> T;

    for(int t = 0; t < T; ++t)
    {
        std::cin >> N >> K;

        int i;
        for(int n = 0; n < N; ++n)
        {
            std::cin >> i;

            d.push_back(i);
            if(d.size() == K)
            {
                std::cout << *max_element(d.begin(), d.end()) << " ";
                d.pop_front();
            }
        }

        std::cout << std::endl;
        d.clear();
    }

    return 0;
}


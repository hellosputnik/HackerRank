#include <deque>
#include <iostream>
#include <set>

int main(int argc, char **argv)
{
    int T;
    int N, K;
    int *A;

    std::deque<int> d;
    std::multiset<int> s;

    std::cin >> T;
    for(int t = 0; t < T; ++t)
    {
        std::cin >> N >> K;
        A = new int[N];

        for(int n = 0; n < N; ++n)
            std::cin >> A[n];

        d = std::deque<int>(&A[0], &A[0] + K);
        s = std::multiset<int>(&A[0], &A[0] + K);

        for(int n = K; n <= N; ++n)
        {
            std::cout << *(s.rbegin()) << " ";

            s.insert(A[n]);
            d.push_back(A[n]);
            s.erase(s.find(d.front()));
            d.pop_front();

        }

        std::cout << std::endl;
    }

    return 0;
}


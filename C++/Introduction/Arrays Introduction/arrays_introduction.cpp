#include <iostream>

int main(int argc, char **argv)
{
    int N;
    int *A;

    std::cin >> N;
    A = new int[N];

    for(int n = 0; n < N; ++n)
        std::cin >> A[n];

    for(int n = (N - 1); n >= 0; --n)
        std::cout << A[n] << " ";

    return 0;
}


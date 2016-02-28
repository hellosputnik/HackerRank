#include <bitset>
#include <iostream>

int main(int argc, char **argv)
{
    using namespace std;

    int N, S, P, Q, a, b;

    cin >> N >> S >> P >> Q;

    bitset<2147483648> *bs = new bitset<2147483648>();

    a = S & 2147483647;
    bs->set(a);

    for(int i = 1; i < N; ++ i)
    {
        b = a * P + Q & 2147483647;

        bs->set(b);

        a = b;
    }

    cout << bs->count() << endl;

    return 0;
}


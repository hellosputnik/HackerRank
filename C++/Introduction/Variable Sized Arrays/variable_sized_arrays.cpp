#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int N, Q;

    cin >> N >> Q;
    int **array = new int*[N];

    for(int n = 0; n < N; ++n)
    {
        int k;

        cin >> k;
        array[n] = new int[k];

        for(int i = 0; i < k; ++i)
            cin >> array[n][i];
    }

    for(int q = 0; q < Q; ++q)
    {
        int a, b;

        cin >> a >> b;
        cout << array[a][b] << endl;
    }

    return 0;
}


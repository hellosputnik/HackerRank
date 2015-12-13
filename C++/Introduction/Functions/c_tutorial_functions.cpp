#include <algorithm>
#include <iostream>

int main(int argc, char **argv)
{
    using namespace std;

    int a, b, c, d;

    cin >> a >> b >> c >> d;
    cout << max(a, max(b, max(c, d))) << endl;

    return 0;
}


#include <cmath>


#include <iostream>
#include <string>


std::string f(int x, int y, int z) {
    // Compare via  subtraction operation.
    int result = std::abs(x - z) - std::abs(y - z);

    // If the difference is negative, then A was closer.
    if (result < 0)
        return "Cat A";

    // If the difference is exactly zero, then the A and B were equidistant.
    if (result == 0)
        return "Mouse C";

    // If the difference is positive, then B was closer.
    if (result > 0)
        return "Cat B";

    return nullptr;
}


int main(int argc, char **argv) {
    int q;

    // Read in the number of queries.
    std::cin >> q;

    // For each query, read the data and print the results.
    for (int i = 0; i < q; ++i) {
        // Read the location of cat A, cat B, and mouse C.
        int x, y, z;
        std::cin >> x >> y >> z;

        // Print the result of the query.
        std::cout << f(x, y, z) << std::endl;
    }

    return 0;
}


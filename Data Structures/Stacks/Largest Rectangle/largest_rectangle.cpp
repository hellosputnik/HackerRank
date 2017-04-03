#include <iostream>
#include <vector>


int main(int argc, char **argv) {
    int N;
    std::vector<int> heights;

    std::cin >> N;

    // Read and save the height of the buildings.
    for (int n = 0; n < N; ++n) {
        int height;

        // Read the height of the n-th building.
        std::cin >> height;

        // Save the height of the n-th building.
        heights.push_back(height);
    }

    for (int height : heights) {
        std::cout << height << " ";
    }

    return 0;
}


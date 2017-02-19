#include <iostream>
#include <set>
#include <stack>


int main(int argc, char **argv) {
    int N;
    std::multiset<int, std::greater<int>> elements;
    std::stack<int> stack;

    std::cin >> N;

    for (int n = 0; n < N; ++n) {
        int query;

        std::cin >> query;

        switch (query) {
            case 1: {
                int x;

                std::cin >> x;
                elements.insert(x);
                stack.push(x);

                break;
            }
            case 2: {
                auto element = elements.find(stack.top());
                elements.erase(element);
                stack.pop();

                break;
            }
            case 3:
                std::cout << *elements.begin() << std::endl;

                break;
            default:
                // This line should never be reached because HackerRank
                // guarantees that each query is valid.
                break;
        }
    }

    return 0;
}


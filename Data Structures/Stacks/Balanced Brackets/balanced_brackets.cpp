#include <iostream>
#include <stack>
#include <string>


bool check(std::string s) {
    std::stack<char> brackets;

    // For each character c in string s, push opening brackets and pop closing
    // brackets.
    for (char &c : s) {
        switch (c) {
            case '{':
            case '(':
            case '[':
                brackets.push(c);
                break;
            case '}':
                if (brackets.empty() || brackets.top() != '{')
                    return false;
                else
                    brackets.pop();
                break;
            case ')':
                if (brackets.empty() || brackets.top() != '(')
                    return false;
                else
                    brackets.pop();
                break;
            case ']':
                if (brackets.empty() || brackets.top() != '[')
                    return false;
                else
                    brackets.pop();
                break;
            default:
                break;
        }
    }

    return brackets.empty();
}

int main(int argc, char **argv) {
    int n;

    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        std::string s;

        std::cin  >> s;
        std::cout << (check(s) ? "YES" : "NO") << std::endl;
    }

    return 0;
}


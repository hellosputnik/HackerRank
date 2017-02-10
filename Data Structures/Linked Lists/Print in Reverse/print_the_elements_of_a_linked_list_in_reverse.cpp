#include <stack>

void ReversePrint(Node *head)
{
    std::stack<int> numbers;

    while (head)
    {
        numbers.push(head->data);
        head = head->next;
    }

    while (!numbers.empty())
    {
        std::cout << numbers.top() << std::endl;
        numbers.pop();
    }
}


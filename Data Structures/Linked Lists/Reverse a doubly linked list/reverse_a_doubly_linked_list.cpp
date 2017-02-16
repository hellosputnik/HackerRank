// This method reverses the original linked list using a stack; this algorithm
// is an in-place algorithm.

#include <stack>

Node* TailInsert(Node *head, Node *node)
{
    Node* pointer = head;
    while (pointer->next)
        pointer = pointer->next;

    pointer->next = node;
    node->next    = NULL;
    node->prev    = pointer;

    return head;
}

Node* Reverse(Node *head) {
    std::stack<Node*> nodes;
    Node* pointer = head;

    if (!head)
        return NULL;

    while (pointer->next) {
        nodes.push(pointer);
        pointer = pointer->next;
    }

    head = pointer;

    while (!nodes.empty()) {
        Node* node = nodes.top();
        nodes.pop();

        TailInsert(head, node);
    }

    return head;
}


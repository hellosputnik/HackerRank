


// This method reverses the original linked list using a stack; this algorithm
// is an in-place algorithm.
/*
#include <stack>

Node* TailInsert(Node *head, Node *node)
{
    if (!head)
        return node;

    Node* pointer = head;
    while (pointer->next)
        pointer = pointer->next;

    pointer->next = node;
    node->next    = NULL;

    return head;
}

Node* Reverse(Node *head) {
    std::stack<Node*> nodes;
    Node* pointer = head;

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
*/


// This method reverses the linked list by creating a new linked list using a
// stack.
/*
#include <stack>

Node* TailInsert(Node *head, int data)
{
    Node* pointer = head;
    Node* node = new Node { data, NULL };

    while (pointer != NULL && pointer->next)
        pointer = pointer->next;

    if (pointer)
        pointer->next = node;
    else
        head = node;

    return head;
}

Node* Reverse(Node *head) {
    std::stack<Node*> nodes;

    while (head->next) {
        nodes.push(head);
        head = head->next;
    }

    while (!nodes.empty()) {
        Node* node = nodes.top();
        nodes.pop();

        TailInsert(head, node->data);
        free(node);
    }

    return head;
}
*/


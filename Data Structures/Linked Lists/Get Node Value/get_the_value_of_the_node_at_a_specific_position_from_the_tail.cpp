int GetNode(Node *head, int positionFromTail) {
    Node* pointer = head;
    Node* forward = head;

    for (int i = 0; i < positionFromTail && forward->next; ++i)
        forward = forward->next;

    while (forward->next) {
        pointer = pointer->next;
        forward = forward->next;
    }

    return pointer->data;
}


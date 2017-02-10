Node* Insert(Node *head, int data)
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


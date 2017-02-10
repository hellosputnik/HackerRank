Node* Insert(Node *head, int data)
{
    Node* pointer = new Node;

    pointer->data = data;
    pointer->next = head;

    return pointer;
}


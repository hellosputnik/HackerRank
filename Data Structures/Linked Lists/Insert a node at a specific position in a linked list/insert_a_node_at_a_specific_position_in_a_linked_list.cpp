Node* InsertNth(Node *head, int data, int position)
{
    // Create the node to insert.
    Node* nthNode = new Node;
    nthNode->data = data;
    nthNode->next = NULL;

    // Handle insertion at the head of the linked list.
    if (position == 0)
    {
        nthNode->next = head;
        return nthNode;
    }

    // Otherwise, navigate to the node prior to the desired insertion position.
    Node* pointer = head;
    for(int i = 0; i < (position - 1) && pointer; ++i)
        pointer = pointer->next;

    // Insert the node.
    if (pointer)
    {
        nthNode->next = pointer->next;
        pointer->next = nthNode;
    } else {
        // TODO: Handle error.
    }

    return head;
}


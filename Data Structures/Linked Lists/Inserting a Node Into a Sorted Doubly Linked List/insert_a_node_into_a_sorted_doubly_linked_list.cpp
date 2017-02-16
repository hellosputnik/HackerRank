Node* SortedInsert(Node *head, int data) {
    // Allocate space for the new node.
    Node *node = new Node;

    // Initialize the data of the node.
    node->data = data;
    node->next = NULL;
    node->prev = NULL;

    // If the head is null, the node becomes the new head.
    if (!head)
        return  node;

    // Handle insertions at the head.
    if (node->data < head->data) {
        head->prev = node;
        node->next = head;
        head = node;

        return head;
    }

    // Traverse to the node before the larger data value (or NULL).
    Node *pointer = head;
    while (pointer->next && node->data > pointer->next->data)
        pointer = pointer->next;

    // Handle insertions in the middle and at the end of the linked list.
    if (pointer->next)
        pointer->next->prev = node;
    node->next = pointer->next;
    node->prev = pointer;
    pointer->next = node;

    return head;
}


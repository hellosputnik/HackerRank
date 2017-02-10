Node* Delete(Node *head, int position)
{
    Node *pointer = head;

    /// Handle deletions at the head of the linked list.
    if (position == 0)
    {
        head = head->next;
        delete pointer;

        return head;
    }

    // Navigate to the position prior to the node to delete.
    for (int i = 0; i < (position - 1) && pointer; ++i)
        pointer = pointer->next;

    // Delete the node.
    if (pointer)
    {
        Node *nodeToDelete = pointer->next;
        pointer->next = pointer->next->next;
        delete nodeToDelete;
    } else {
        // TODO: Handle error.
    }

    return head;
}


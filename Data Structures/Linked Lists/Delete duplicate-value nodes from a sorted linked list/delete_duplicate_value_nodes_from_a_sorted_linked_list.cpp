Node* RemoveDuplicates(Node *head) {
    Node *pointer = head;

    while (pointer->next) {
        if (pointer->data == pointer->next->data) {
            Node *duplicate = pointer->next;
            pointer->next = duplicate->next;
            delete duplicate;
        }
        else {
            pointer = pointer->next;
        }
    }

    return head;
}


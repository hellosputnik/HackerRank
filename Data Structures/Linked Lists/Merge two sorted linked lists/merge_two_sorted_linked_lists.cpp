Node* MergeLists(Node *headA, Node *headB) {
    Node *head = NULL;

    if (!headA)
        return headB;

    if (!headB)
        return headA;

    if (headA->data < headB->data) {
        head = headA;
        headA = headA->next;
    } else {
        head = headB;
        headB = headB->next;
    }

    Node* pointer = head;
    while (headA && headB) {
        if (headA->data < headB->data) {
            pointer->next = headA;
            headA = headA->next;
        }
        else {
            pointer->next = headB;
            headB = headB->next;
        }
        pointer = pointer->next;
    }

    if (headA)
        pointer->next = headA;
    else
        pointer->next = headB;

    return head;
}


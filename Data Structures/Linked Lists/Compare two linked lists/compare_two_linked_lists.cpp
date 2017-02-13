int CompareLists(Node *headA, Node *headB) {
    Node *pointerA = headA;
    Node *pointerB = headB;

    while (pointerA && pointerB) {
        if (pointerA->data != pointerB->data)
            return 0;
        pointerA = pointerA->next;
        pointerB = pointerB->next;
    }

    return pointerA == pointerB ? 1 : 0;
}


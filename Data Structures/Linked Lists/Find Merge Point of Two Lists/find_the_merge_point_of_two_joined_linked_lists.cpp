#include <map>


int FindMergeNode(Node *headA, Node *headB) {
    std::map<Node*, bool> addresses;

    while (headA) {
        Node *address = headA;

        addresses[address] = true;

        headA = headA->next;
    }

    while (headB) {
        Node *address = headB;

        if (addresses.find(address) != addresses.end())
            break;

        headB = headB->next;
    }

    return headB->data;
}


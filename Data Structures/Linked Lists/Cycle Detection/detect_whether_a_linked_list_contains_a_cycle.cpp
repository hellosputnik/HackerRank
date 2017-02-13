#include <map>

bool has_cycle(Node *head) {
    // We need a node pointer to traverse the linked list and a map to log all
    // the nodes we have seen.
    Node *pointer = head;
    std::map<Node*, bool> addresses;

    // Loop through the linked list.
    while (pointer) {
        // Get the memory address of the node.
        Node *address = pointer;

        // If the memory address is in the map, we have already seen it.
        // Otherwise, add it to the map to keep track of it.
        if (addresses.find(address) != addresses.end())
            return true;
        else
            addresses[address] = true;

        // Move onto the next node.
        pointer = pointer->next;
    }

    // This section of the code can only be reached if the linked list ended.
    // In other words, the linked list has no loop.
    return false;
}


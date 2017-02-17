#include <queue>


node* lca(node *root, int v1, int v2) {
    std::queue<node*> path1;
    std::queue<node*> path2;
    node *pointer;

    // Build the path to v1.
    pointer = root;
    while (pointer->data != v1) {
        // Add the node to the path to v1.
        path1.push(pointer);

        // v1 is less than the data at the current node; go left.
        if (v1 < pointer->data)
            pointer = pointer->left;
        // v1 is more than the data at the current node; go right.
        else
            pointer = pointer->right;
    }
    path1.push(pointer);

    // Build the path to v2.
    pointer = root;
    while (pointer->data != v2) {
        // Add the node to the path to v1.
        path2.push(pointer);

        // v2 is less than the data at the current node; go left.
        if (v2 < pointer->data)
            pointer = pointer->left;
        // v2 is more than the data at the current node; go right.
        else
            pointer = pointer->right;
    }
    path2.push(pointer);

    while (path1.front() == path2.front()) {
        pointer = path1.front();

        path1.pop();
        path2.pop();
    }

    return pointer;
}


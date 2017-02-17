bool check(Node *node, int min, int max) {
    if (node == NULL)
        return true;

    if (node->data < min || node->data > max)
        return false;

    return check(node->left,  min, node->data - 1) &
           check(node->right, node->data + 1, max);
}

bool checkBST(Node *root) {
    return check(root, 0, 10000);
}


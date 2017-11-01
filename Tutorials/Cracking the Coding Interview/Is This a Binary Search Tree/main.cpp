bool check(Node *n, int min, int  max) {
    if (n == nullptr)
        return true;

    if (n->data <= min || n->data >= max)
        return false;

    return check(n->left,  min, n->data) &&
           check(n->right, n->data, max);
}

bool checkBST(Node *root) {
    if (root == nullptr)
        return true;

    return check(root, -1, 10001);
}

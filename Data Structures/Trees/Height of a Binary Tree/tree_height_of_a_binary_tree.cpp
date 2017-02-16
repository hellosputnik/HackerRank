int max(int a, int b) {
    return a > b ? a : b;
}

int height(Node *node, int depth) {
    if (!node)
        return depth;

    ++depth;
    return max(height(node->left,  depth), height(node->right, depth));
}

int height(Node *root) {
    return (height(root, 0) - 1);
}


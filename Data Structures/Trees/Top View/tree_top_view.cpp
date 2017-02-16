void top_view_left(node *node) {
    if (!node)
        return;

    top_view_left(node->left);
    std::cout << node->data << " ";
}

void top_view_right(node *node) {
    if (!node)
        return;

    std::cout << node->data << " ";
    top_view_right(node->right);
}

void top_view(node *root) {
    if (!root)
        return;

    top_view_left(root->left);
    std::cout << root->data << " ";
    top_view_right(root->right);
}


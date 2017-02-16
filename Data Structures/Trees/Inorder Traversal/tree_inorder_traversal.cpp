void inOrder(node *root) {
    if (!root)
        return;

    inOrder(root->left);
    std::cout << root->data << " ";
    inOrder(root->right);
}


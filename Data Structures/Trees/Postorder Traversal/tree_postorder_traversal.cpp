void postOrder(node *root) {
    if (!root)
        return;

    postOrder(root->left);
    postOrder(root->right);

    std::cout << root->data << " ";
}

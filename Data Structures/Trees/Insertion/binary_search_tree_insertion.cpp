node* insert(node *root, int value) {
    node *n;

    if (root == NULL) {
        n = new node;

        n->data  = value;
        n->left  = NULL;
        n->right = NULL;

        root = n;
    }

    else {
        // If the value is less than the current node, try to insert left.
        if (value < root->data) {
            if (root->left)
                insert(root->left, value);
            else {
                n = new node;

                n->data  = value;
                n->left  = NULL;
                n->right = NULL;

                root->left = n;
            }
        }
        // If the value is more than the current node, try to insert right.
        else {
            if (root->right)
                insert(root->right, value);
            else {
                n = new node;

                n->data  = value;
                n->left  = NULL;
                n->right = NULL;

                root->right = n;
            }
        }

    }

    return root;
}


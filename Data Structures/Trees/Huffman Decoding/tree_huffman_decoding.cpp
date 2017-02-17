bool is_leaf(node *n) {
    return (n->left || n->right) ? false : true;
}

void decode_huff(node *root, string s) {
    string decoded_string;
    node *pointer = root;

    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == '0') {
            if (is_leaf(pointer->left)) {
                decoded_string += pointer->left->data;
                pointer = root;
                continue;
            }
            pointer = pointer->left;
        }
        else {
            if (is_leaf(pointer->right)) {
                decoded_string += pointer->right->data;
                pointer = root;
                continue;
            }
            pointer = pointer->right;
        }
    }

    std::cout << decoded_string << std::endl;
}


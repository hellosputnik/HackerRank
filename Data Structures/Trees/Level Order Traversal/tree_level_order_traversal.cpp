#include <queue>


void LevelOrder(node *root) {
    if (root == NULL)
        return;

    std::queue<node*> q;
    q.push(root);

    while (!q.empty()) {
        node *n = q.front();
        std::cout << n->data << " ";
        q.pop();

        if (n->left)
            q.push(n->left);

        if (n->right)
            q.push(n->right);
    }
}


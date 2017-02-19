#include <cmath>


#include <iostream>
#include <map>
#include <queue>
#include <vector>


struct Node {
    int data;
    int depth;

    Node *left;
    Node *right;

    Node(int data, int depth) : data(data), depth(depth) {
        left  = nullptr;
        right = nullptr;
    }

    void swap() {
        Node *temporary = left;

        left  = right;
        right = temporary;
    }
};

struct Tree {
    Node *root;
    std::map<int, std::vector<Node*>> table;

    void print() {
        InOrderPrint(root);
    }

    void InOrderPrint(Node *node) {
        if (node == nullptr)
            return;

        InOrderPrint(node->left);
        std::cout << node->data << " ";
        InOrderPrint(node->right);
    }
};


int main(int argc, char **argv) {

    // ==== Binary tree creation phase =========================================
    int N;
    std::queue<Node*> nodes;
    Node *root;
    Tree tree;

    // Get the number of nodes to read. The next N-lines will also be the
    // children of the n-th node.
    std::cin >> N;

    // Create a root node, add it to the tree, and add the root to the queue to
    // add children nodes (or NULL nodes).
    root = new Node(1, 1);
    tree = { root };
    nodes.push(root);

    // Add the root node to the depth table.
    tree.table[1].push_back(root);

    // Get the remaining nodes.
    for (int n = 0; n < N; ++n) {
        // Get the parent node.
        Node *node = nodes.front();
        nodes.pop();

        // Read and add the children node to the parent node.
        int left, right, depth;

        std::cin >> left;
        std::cin >> right;
        depth = node->depth + 1;

        node->left  = left  == -1 ? nullptr : new Node(left,  depth);
        node->right = right == -1 ? nullptr : new Node(right, depth);

        // Add the children nodes to the queue and table.
        if (node->left != nullptr) {
            nodes.push(node->left);
            tree.table[depth].push_back(node->left);
        }
        if (node->right != nullptr) {
            nodes.push(node->right);
            tree.table[depth].push_back(node->right);
        }
    }
    // =========================================================================


    // ==== Node swapping phase ================================================
    int T;

    // Get the number of swap operations.
    std::cin >> T;

    for (int t = 0; t < T; ++t) {
        int K;

        // Get the depth that needs to be swapped.
        std::cin >> K;

        // Calculate the max depth, h, read the table of nodes at K-depth, and
        // swap the children.
        for (int k = K; k <= N; k += K)
            for (auto node : tree.table[k])
                node->swap();

        // In-order print the tree.
        tree.print();
        std::cout << std::endl;
    }
    // =========================================================================

    return 0;
}


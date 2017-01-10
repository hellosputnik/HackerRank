class SumInLeavesVisitor extends TreeVis {
    private int result;

    public SumInLeavesVisitor() {
        result = 0;
    }

    public int getResult() {
        return result;
    }

    public void visitNode(TreeNode node) {
    }

    public void visitLeaf(TreeLeaf leaf) {
        result += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    private long result;
    private final int M = 1000000007;

    public ProductOfRedNodesVisitor() {
        result = 1;
    }

    public int getResult() {
        return (int)result;
    }

    public void visitNode(TreeNode node) {
        if (node.getColor().equals(Color.RED))
            result = (result * node.getValue()) % M;
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor().equals(Color.RED))
            result = (result * leaf.getValue()) % M;
    }
}

class FancyVisitor extends TreeVis {
    private int result;
    private int nodes;
    private int leaves;

    public FancyVisitor() {
        result = 0;
    }

    public int getResult() {
        result = Math.abs(nodes - leaves);
        return result;
    }

    public void visitNode(TreeNode node) {
        if (node.getDepth() % 2 == 0)
            nodes += node.getValue();
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor().equals(Color.GREEN))
            leaves += leaf.getValue();
    }
}

public class Solution {

    private static int x[];
    private static Color c[];
    private static Map<Integer, Set<Integer>> nodesMap = new HashMap<>();

    public static Tree solve() {
        Scanner cin = new Scanner(System.in);

        int N = cin.nextInt();

        x = new int[N];
        for(int index = 0; index < N; index++) {
            x[index] = cin.nextInt();
        }

        c = new Color[N];
        for(int index = 0; index < N; index++) {
            c[index] = (cin.nextInt() == 0) ? Color.RED : Color.GREEN;
        }

        Tree rootNode;
        if(N == 1) {
            rootNode = new TreeLeaf(x[0], c[0], 0);
        }
        else {
            for(int index = 0; index < (N - 1); index++) {
                int u = cin.nextInt();
                int v = cin.nextInt();
                Set<Integer> uEdges = nodesMap.get(u);
                if(uEdges == null) {
                    uEdges = new HashSet<>();
                }
                uEdges.add(v);
                nodesMap.put(u, uEdges);
                Set<Integer> vEdges = nodesMap.get(v);
                if(vEdges == null) {
                    vEdges = new HashSet<>();
                }
                vEdges.add(u);
                nodesMap.put(v, vEdges);
            }

            rootNode = new TreeNode(x[0], c[0], 0);
            Set<Integer> rootEdges = nodesMap.get(1);
            Iterator<Integer> rootIterator = rootEdges.iterator();
            while(rootIterator.hasNext()) {
                Integer nodeIdentifier = rootIterator.next();
                nodesMap.get(nodeIdentifier).remove(1);
                createEdge(rootNode, nodeIdentifier);
            }
        }

        return rootNode;
    }

    private static void createEdge(Tree parentNode, Integer nodeIdentifier) {

        Set<Integer> nodeEdges = nodesMap.get(nodeIdentifier);
        boolean hasChild = false;
        if(nodeEdges != null && !nodeEdges.isEmpty())
            hasChild = true;

        if(hasChild) {
            TreeNode node = new TreeNode(x[nodeIdentifier - 1], c[nodeIdentifier - 1], parentNode.getDepth() + 1);
            ((TreeNode) parentNode).addChild(node);
            Iterator<Integer> nodeIterator = nodeEdges.iterator();
            while(nodeIterator.hasNext()) {
                Integer neighborNodeIdentifier = nodeIterator.next();
                nodesMap.get(neighborNodeIdentifier).remove(nodeIdentifier);
                createEdge(node, neighborNodeIdentifier);
            }
        }
        else {
            TreeLeaf leaf = new TreeLeaf(x[nodeIdentifier - 1], c[nodeIdentifier - 1], parentNode.getDepth() + 1);
            ((TreeNode) parentNode).addChild(leaf);
        }
    }

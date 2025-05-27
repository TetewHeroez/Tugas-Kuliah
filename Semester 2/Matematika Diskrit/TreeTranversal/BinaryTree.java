class Node {
  char data;
  Node left, right;

  public Node(char data) {
      this.data = data;
      left = right = null;
  }
}


public class BinaryTree {
    Node root;

    BinaryTree() {
        root = null;
    }

    void PostOrder(Node node) {
        if (node == null)
            return;

        // Traverse the left subtree
        PostOrder(node.left);

        // Traverse the right subtree
        PostOrder(node.right);

        // Visit the node
        System.out.print(node.data + " ");
    }

    void InOrder(Node node) {
        if (node == null)
            return;

        // Traverse the left subtree
        InOrder(node.left);

        // Visit the node
        System.out.print(node.data + " ");

        // Traverse the right subtree
        InOrder(node.right);
    }

    void PreOrder(Node node) {
        if (node == null)
            return;

        // Visit the node
        System.out.print(node.data + " ");

        // Traverse the left subtree
        PreOrder(node.left);

        // Traverse the right subtree
        PreOrder(node.right);
    }
}

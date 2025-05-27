public class Main {
  public static void main(String[] args) {
    BinaryTree tree = new BinaryTree();
    tree.root = new Node('A');
    tree.root.left = new Node('B');
    tree.root.right = new Node('C');
    tree.root.left.left = new Node('D');
    tree.root.left.right = new Node('E');
    tree.root.right.left = new Node('F');
    tree.root.right.right = new Node('G');

    System.out.println("Preorder traversal of binary tree is:");
    tree.PreOrder(tree.root);

    System.out.println("\nInorder traversal of binary tree is:");
    tree.InOrder(tree.root);

    System.out.println("\nPostorder traversal of binary tree is:");
    tree.PostOrder(tree.root);
  }
}

Tree is a hirarchical data structure
Travesal - 2 Types

Level-order Traversal = Root left right

Depth first Search
    - Inorder Traversal     => Left - [Root] - Right
    - Preorder Traversal    => [Root] - Left - Right 
    - Postorder Traversal   => Left - Right - [Root]

Each node "V" is inserted a index "i" as per below concept
 - If V is root, i = 1 

formula to find out left child:
 -> 2*i 

formula to find right child:
 -> 2*i + 1
 
formula to find parents
 -> (i-1)//2

BST Delete
3 cases: 
    Delete node with no children
    Delete node with one child
    Delete node with two children 

Delete node with 2 children:
    - Find out and replace the node with inorder predicisor which is at it's left subtree
    - It is a value which is th biggest number. That value will be present at the least right leaf node
    - Or fo with inorder successor, it is at the right subtree.
    - It is the smallest value in that subtree which will be present as least left node.

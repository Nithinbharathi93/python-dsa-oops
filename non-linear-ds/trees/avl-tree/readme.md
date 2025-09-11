When BST becomes a skewed tree, searching for a particular element especially the leaf-node will make it as a linear search and it ends up with less effeciency. 
So in order to maintain the effeciency, we need to make the tree as balanced tree.

>[!NOTE]
>When we are trying to create a balanced tree, we are reducing the height of the tree

Definition:
* It should be a BST
* Balance Fatcor (BF) for every node should be either `0`, `1`, or `-1`. Else we have to balance the tree

Calculating the Balance Factor:
* Balance factor = Height(left subtree) - Height(right subtree)

```mermaid
graph TD
    A[50]
    B[30]
    C[60]
    D[20]
    E[45]
    F[55]
    G[70]
    H[75]
    I[80]

    A --> B
    A --> C
    B --> D
    B --> E
    C --> F
    C --> G
    G --> H
    H --> I
```
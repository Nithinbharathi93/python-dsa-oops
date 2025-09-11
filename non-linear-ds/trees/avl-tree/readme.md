# AVL Tree

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

* 50's balance factor = 2-4 = -2
* 30's balance factor = 1-1 = 0
* 60's balance factor = 1-3 = -2
* 70's balance factor = 0-2 = -2
* 75's balance factor = 0-1 = -1

The nodes `50`, `60`, and `70` are confilicting with the AVL rules. <br>
These nodes are called **Critical Node**. <br>
**Reason:** The balance factor is not 0, 1, or -1. <br>


## AVL rotations

* RR rotation - Right Right
* LL rotation - Left Left
* LR rotation - Left Right
* RL rotation - Right Left

> [!NOTE]
> RR and LL are single rotations <br>
> RL and LR are double rotations

## AVL Construction

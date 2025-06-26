# Portfolio Assessment knowledge questions

## Step 1 - Describe what a Binary Search Tree (BST) is

> A binary search tree is a specific type of tree that has two children.  
> All children on the left side are less than the parent node, and all children on the right are greater than the parent nodes.

## Step 2 - How to find an item in a Binary Search Tree

> Finding an item in a binary search tree requires an algorithm that starts at the apex node (the root) and compares the node's value with the target value.  
> If the target is more than the node's value the selected node will move the child on the right; else it will move to the child on the left.  
> This process repeats recursively until the value is reached or the maximum depth is reached indicating that the target value is not contained in the tree.

## Step 3 - Describe what a balanced BST is

> A balanced binary search tree is a BST with the depth of the left and right subtrees differing by no more than one.

## Step 8 - Max steps to Find an Existing item

> With 4 items in the tree the maxiumum amount of steps it could to find an item is the same as the Height.  
> for this example with 4 items. if the tree is completely unbalance it could take 4 steps including the root.  
> if the tree was balanced it would take a max of 3 steps to find the item including the root.  
> the time complexisty of searching in a balanced tree is O(log n)

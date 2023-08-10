
# Type of Trees
## Binary Tree

# Basic Operations

## Recursive Traversal
A basic operation is recursive to traverse the tree. The following code is a recursive traversal of a binary tree.

```python DFS   
def traverse(root):
    if root is None:
        return
    traverse(root.left)
    traverse(root.right)
```

```python BFS
def traverse(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```


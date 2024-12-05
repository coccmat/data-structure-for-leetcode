from graphviz import Digraph
def render_binary_tree(root, highlight=None):
    """
    Render a binary tree using Graphviz.
    """
    graph = Digraph(format='png')
    if not root:
        return graph

    frontier = deque([root])

    while frontier:
        node = frontier.popleft()
        if node:
            label = f"{node.val}"
            if node == highlight:
                graph.node(str(id(node)), label, style="filled", color="red")
            else:
                graph.node(str(id(node)), label)

            if node.left:
                frontier.append(node.left)
                graph.edge(str(id(node)), str(id(node.left)))
            if node.right:
                frontier.append(node.right)
                graph.edge(str(id(node)), str(id(node.right)))

    return graph


def print_tree(node, level=0):
    """
    Print a binary tree to the terminal.
    """
    if node:
        print(' ' * (4 * level) + f"Node({node.val})")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)

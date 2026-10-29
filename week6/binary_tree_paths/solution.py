class Solution:
    def binaryTreePaths(self, root):
        paths = []

        def build_paths(node, path):
            if node is None:
                return

            if path == "":
                path = str(node.val)
            else:
                path = path + "->" + str(node.val)

            if node.left is None and node.right is None:
                paths.append(path)
                return

            build_paths(node.left, path)
            build_paths(node.right, path)

        build_paths(root, "")
        return paths

# Taks 1-2: Print Binary Tree Nodes


def print_binary_tree(tree):
    # Pre-order DFS
    print(tree["value"])
    if tree["left"]:
        print_binary_tree(tree["left"])
    if tree["right"]:
        print_binary_tree(tree["right"])


def main():
    tree = {
        "value": 1,
        "left": {
            "value": 5,
            "left": None,
            "right": {"value": 7, "left": None, "right": None},
        },
        "right": {
            "value": 10,
            "left": {"value": 8, "left": None, "right": None},
            "right": {"value": 15, "left": None, "right": None},
        },
    }
    print_binary_tree(tree)


if __name__ == "__main__":
    main()

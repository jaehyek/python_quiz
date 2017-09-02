from binarytree import tree, convert, pprint

def FindNodeAtSameLevel(node,level, result):
    if not node:
        return -1
    if len(result) < level + 1:
        result.append([])
    result[level].append(node.value)
    FindNodeAtSameLevel(node.left, level + 1, result)
    FindNodeAtSameLevel(node.right, level + 1, result)


my_list = [aa for aa in range(30)]
my_tree = convert(my_list)
my_tree.show()
result = []
FindNodeAtSameLevel(my_tree,0, result)

# print the list node at level 3
print(result[3])

# print the list node at level 4
print(result[4])
# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    
    # if i is less than the length of the list
    if i < len(my_list):
        # print "i'th" item of list
        print my_list[i]
        # recursive call list and increment 1
        print_item(my_list, i+1)



# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    # print the tree (current node)'s data
    print tree.data
    # for each of the current node's children
    for child in tree.children:
        # print the child's data
        # call the print_all_tree data function
        # pass in the child as the tree/current node
        print_all_tree_data(child)
    

# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    # if not empty list
    if not my_list:
        # return 0
        return 0
    # return 1 + everything in list except first item
    return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """

    # node count starts at 1, we want to count the ree node
    node_count = 1
    # go through each child in the tree node
    for child in tree.children:
        # increment node_count + call num_nodes with new child/tree node        
        node_count = node_count + num_nodes(child)
    return node_count

    # take the length of children's list and add +1 for current node

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

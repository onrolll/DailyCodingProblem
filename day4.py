"""
Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    """ serializes a node to a string """
    return_arr = ['']
    req_serialize(node, return_arr)
    return_string = ' '.join(return_arr)
    return return_string

def req_serialize(node, return_arr):
    """ recursive call for serialize method """
    return_arr.append("Node(")
    return_arr.append(node.val)
    
    if(node.left != None):
        req_serialize(node.left, return_arr)
    if(node.right != None):
        req_serialize(node.right, return_arr)
    return_arr.append(')')
    return

def deserialize(node_string):
    """ deserialize a node back from string 
     Node( root Node( left Node( left.left ) ) Node( right ) )
    """
    """['Node(', 'root', 
            'Node(', 'left', 
                    'Node(', 'left.left', ')',
                     --should have right node--')', 
            'Node(', 'right',
                     --sh h ln--,
                     --sh h rn--')', 
        ')']
    """

    node_arr = node_string.split(' ')
    node_arr = [x for x in node_arr if x != '']
    node, node_arr = req_deserialize(node_arr)

    return node


def req_deserialize(node_arr):
    if(node_arr[0] != 'Node('):
        return None, node_arr
    node = Node(node_arr[1])
    node_arr = node_arr[2:]
    

    node.left, node_arr = req_deserialize(node_arr)
    node.right, node_arr = req_deserialize(node_arr)

    node_arr = node_arr[1:]

    return node, node_arr




if __name__ == '__main__':

    node = Node('root', Node('left', Node('left.left'), Node('left-right')), Node('right'))
    ser_node = serialize(node)
    des_node = deserialize(ser_node)
    print(des_node.left.left.val)
    print(ser_node)
    deserialize(ser_node)
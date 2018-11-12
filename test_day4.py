import unittest
from day4 import Node, serialize, deserialize
class TestSerializeDeserializeNode(unittest.TestCase):
    def testSerializeDeserializeNode(self):
        node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left' 
        assert deserialize(serialize(node)).left.right.val == 'left.right'
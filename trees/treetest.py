from tree import BinaryTreeNode
import pdb

def test_traversals():
  root = BinaryTreeNode(data=0)
  root.left = BinaryTreeNode(1)
  root.left.left = BinaryTreeNode(3)
  root.left.right = BinaryTreeNode(4)
  root.right = BinaryTreeNode(2)
  root.right.left = BinaryTreeNode(5)
  traversal_record = []

  root.record_in_order_traversal(root, traversal_record)
  assert traversal_record == [3, 1, 4, 0, 5, 2]

  traversal_record.clear()
  root.record_pre_order_traversal(root, traversal_record)
  assert traversal_record == [0, 1, 3, 4, 2, 5]

  traversal_record.clear()
  root.record_post_order_traversal(root, traversal_record)
  assert traversal_record == [3, 4, 1, 5, 2, 0]



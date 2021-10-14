import random
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
  root.record_in_order_traversal(traversal_record)
  assert traversal_record == [3, 1, 4, 0, 5, 2]

  traversal_record.clear()
  root.record_pre_order_traversal(traversal_record)
  assert traversal_record == [0, 1, 3, 4, 2, 5]

  traversal_record.clear()
  root.record_post_order_traversal(traversal_record)
  assert traversal_record == [3, 4, 1, 5, 2, 0]

def test_route_finder():
  origin = DGNode()
  destination = DGNode()

  # Build a set of spokes, including a one-way path from origin to destination
  for i in range(0,5):
    origin.neighbours.append(DGNode(i))
  for i in range(5,15):
    intermediary = random.choice(origin.neighbours)
    intermediary.neighbours.append(DGNode)
    if i == 14:
      intermediary.neighbours[-1].append(destination)

  assert origin.has_path_to(destination)
  assert destination.has_path_to(origin) == False

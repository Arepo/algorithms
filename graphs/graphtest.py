from directed_graph import DGNode
import random
from tree import BinaryTreeNode
from queue import Queue
import pdb

def test_traversals():
  root = BinaryTreeNode(0)
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
  # pdb.set_trace()
  # Build a set of spokes, including a one-way path from origin to destination
  for i in range(0,5):
    origin.children.append(DGNode(i))
  for i in range(5,15):
    intermediary = random.choice(origin.children)
    intermediary.children.append(DGNode())
    if i == 14:
      # pdb.set_trace()
      intermediary.children[-1].children.append(destination)

  assert origin.has_path_to(destination)
  assert destination.has_path_to(origin) == False

def test_link_equivalent_depths():
  # Build a linked list for each layer
  root = build_balanced_tree_of_size(25)
  # pdb.set_trace()
  lists = root.linked_lists_of_sublayers()
  assert lists[0].data.data == 0
  assert lists[4].data.data == 15
  assert lists[4].end_node().data.data == 24

def test_is_balanced_tree():
  # balanced_root = build_balanced_tree_of_size(13)
  # assert balanced_root.is_balanced_tree()

  unroot = BinaryTreeNode('level 0')
  unroot.left = BinaryTreeNode('level 1 leaf')
  unroot.right = BinaryTreeNode('level 1')
  unroot.right.left = BinaryTreeNode('level 2')
  unroot.right.right = BinaryTreeNode('level 2')
  unroot.right.right.right = BinaryTreeNode('level 3 leaf')

  assert not unroot.is_balanced_tree()


####

def build_balanced_tree_of_size(n):
  children = Queue()

  for i in range(0,n):
    children.put(BinaryTreeNode(i))

  parents = Queue()
  root = current_node = children.get()

  while not children.empty():
    current_node.left = children.get()
    parents.put(current_node.left)
    current_node.right = children.get()
    parents.put(current_node.right)
    current_node = parents.get()
  return root

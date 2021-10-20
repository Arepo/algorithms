from directed_graph import DGNode
import random
from tree import BinaryTreeNode, TreeUtils
from collections import deque, Counter
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
  # Build a set of spokes, including a one-way path from origin to destination
  for i in range(0,5):
    origin.children.append(DGNode(i))
  for i in range(5,15):
    intermediary = random.choice(origin.children)
    intermediary.children.append(DGNode())
    if i == 14:
      intermediary.children[-1].children.append(destination)

  assert origin.has_path_to(destination)
  assert destination.has_path_to(origin) == False

def test_link_equivalent_depths():
  # Build a linked list for each layer
  root = build_balanced_tree_of_size(25)
  lists = root.linked_lists_of_sublayers()
  assert lists[0].data.data == 0
  assert lists[4].data.data == 15
  assert lists[4].end_node().data.data == 24

def test_is_balanced_tree():
  # Check if binary tree is balanced without using a tree wrapper class or top-level functions
  balanced_root = build_balanced_tree_of_size(13)
  assert balanced_root.is_balanced_tree()

  unroot = BinaryTreeNode('level 0')
  unroot.left = BinaryTreeNode('level 1 leaf')
  unroot.right = BinaryTreeNode('level 1')
  unroot.right.left = BinaryTreeNode('level 2')
  unroot.right.right = BinaryTreeNode('level 2')
  unroot.right.right.right = BinaryTreeNode('level 3 leaf')

  assert not unroot.is_balanced_tree()

def test_is_search_tree():
  # Check if binary tree is a search tree without using a tree wrapper class or top-level functions
  non_search_root = build_balanced_tree_of_size(20)
  assert not non_search_root.is_search_tree()

  search_root = BinaryTreeNode(4)
  search_root.left = BinaryTreeNode(2)
  search_root.left.left = BinaryTreeNode(0)
  search_root.left.left.right = BinaryTreeNode(1)
  search_root.left.right = BinaryTreeNode(3)
  search_root.right = BinaryTreeNode(6)
  search_root.right.left = BinaryTreeNode(5)
  assert search_root.is_search_tree()

def test_is_subtree():
  minimal_left_tree = build_balanced_tree_of_size(3)
  extended_left_tree = build_balanced_tree_of_size(3)
  extended_left_tree.left.left = (BinaryTreeNode(18))

  right_tree = build_balanced_tree_of_size(2)
  supertree = BinaryTreeNode(-1)
  supertree.left = extended_left_tree
  supertree.right = right_tree

  utils = TreeUtils()
  assert not utils.is_subtree(right_tree, minimal_left_tree)
  assert not utils.is_subtree(minimal_left_tree, extended_left_tree)
  assert utils.is_subtree(supertree, minimal_left_tree)

def test_random_node_in_binary_search_tree():
  utils = TreeUtils()
  root = utils.build_binary_search_tree(range(1, 4))
  assert root.random_subnode().data in range(1,19)


####

def build_balanced_tree_of_size(n):
  children = deque()

  for i in range(0,n):
    children.appendleft(BinaryTreeNode(i))

  parents = deque()
  root = current_node = children.pop()

  while children:
    current_node.left = children.pop()
    parents.appendleft(current_node.left)
    if not children:
      break
    current_node.right = children.pop()
    parents.appendleft(current_node.right)
    current_node = parents.pop()
  return root

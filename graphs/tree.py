import os
import sys
import inspect
import random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from linked_list import SinglyLinkedList
from linked_list_node import LinkedListNode
from collections import deque
import pdb

class TreeUtils():
  def __init__(self):
    self.root = None

  def is_subtree(self, supertree_root, subtree_root):
    if not subtree_root:
      return True

    if not supertree_root:
      return False

    if (
      supertree_root.data == subtree_root.data                and
      self.is_subtree(supertree_root.left, subtree_root.left) and
      self.is_subtree(supertree_root.right, subtree_root.right)
    ):
      return True

    return self.is_subtree(supertree_root.left, subtree_root) or self.is_subtree(supertree_root.right, subtree_root)

  def build_binary_search_tree(self, defined_range):
    values = list(defined_range)
    random.shuffle(values)
    for value in values:
      self.insert(value)
    return self.root

  def insert(self, value):
    current = self.root
    if not current:
      self.root = BinaryTreeNode(value)
      return

    while current:
      current.subtree_size += 1
      parent = current
      if value < current.data:
        current = current.left
      elif value > current.data:
        current = current.right
      else:
        raise Exception("We're not prepared for this sort of anarchy")

    node = BinaryTreeNode(value)
    if value < parent.data:
      parent.left = node
    else:
      parent.right = node



class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.layer = None
    self.subtree_size = 1

  def __str__(self):
    return "Node <{}>".format(self.data)

  def __repr__(self):
    return "Node <{}>".format(self.data)

  def random_subnode(self, number=None):
    if not number:
      number = random.randint(1, self.subtree_size)
    left_subtree_size = self.left.subtree_size if self.left else 0

    if number <= left_subtree_size:
      return self.left.random_subnode(number)
    if number == self.subtree_size:
      return self
    return self.right.random_subnode(number - left_subtree_size - 1)

  def record_in_order_traversal(self, traversal_record):
    if self.left:
      self.left.record_in_order_traversal(traversal_record)
    traversal_record.append(self.data)
    if self.right:
      self.right.record_in_order_traversal(traversal_record)

  def record_pre_order_traversal(self, traversal_record):
    traversal_record.append(self.data)
    if self.left:
      self.left.record_pre_order_traversal(traversal_record)
    if self.right:
      self.right.record_pre_order_traversal(traversal_record)

  def record_post_order_traversal(self, traversal_record):
    if self.left:
      self.left.record_post_order_traversal(traversal_record)
    if self.right:
      self.right.record_post_order_traversal(traversal_record)
    traversal_record.append(self.data)

  def linked_lists_of_sublayers(self):
    linked_lists = []
    children = deque()
    current_node = self
    children.appendleft(current_node)
    # TODO - clear layers after use
    current_node.layer = 0
    linked_lists.append(LinkedListNode(data=current_node))

    while children:
      current_node = children.pop()

      if current_node.left:
        current_node.left.layer = current_node.layer + 1
        children.appendleft(current_node.left)
      if current_node.right:
        current_node.right.layer = current_node.layer + 1
        children.appendleft(current_node.right)

      if not children:
        break

      next_node = children[-1]

      if next_node.layer != current_node.layer:
        linked_lists.append(LinkedListNode(data=next_node))
      else:
        linked_lists[next_node.layer].append(LinkedListNode(data=next_node))

    return linked_lists

  def is_balanced_tree(self):
    if not self.left and not self.right:
      return [0, 0]
    if not self.left:
      return self.__balance(self.right)
    if not self.right:
      return self.__balance(self.left)

    left_result = heights = self.left.is_balanced_tree()
    right_result = self.right.is_balanced_tree()
    if not left_result:
      return left_result
    if not right_result:
      return right_result

    heights.extend(right_result)
    shortest = min(heights)
    tallest = max(heights)
    if tallest - shortest <= 1:
      return [shortest + 1, tallest + 1]

    return Unbalanced()

  def is_search_tree(self, side=None):
    # TODO may need edge case for when root has 0-1 children
    if not side and self.left.is_search_tree(side='l') < self.data and self.data < self.right.is_search_tree(side='r'):
      # No side means it's the root node of the traversal
      return True
    if not side:
      return False

    # Leaf node
    if not self.left and not self.right:
      return self.data

    # Not root node or leaf node
    if self.left:
      left_value = self.left.is_search_tree(side='l')
    if self.right:
      right_value = self.right.is_search_tree(side='r')

    # Having right child only
    if not self.left and self.data > right_value:
      return NonSearchy()
    if not self.left and side == 'l':
      # Parents of left children care about the child subtree's max value
      return right_value
    if not self.left and side == 'r':
      # Parents of right children care about the child subtree's min value
      return self.data

    # Having left child only
    if not self.right and left_value > self.data:
      return NonSearchy()
    if not self.right and side == 'l':
      return self.data
    if not self.right and side == 'r':
      return left_value

    # Having two children
    if not left_value < self.data or not self.data < right_value:
      return NonSearchy()
    if side == 'l':
      return right_value
    return left_value

  def __balance(self, child):
    balance = child.is_balanced_tree()
    balance[0] += 1
    balance[1] += 1
    return balance

class Unbalanced:
  def extend(self, other):
    return self

  def __bool__(self):
    return False

  def __gt__(self, other):
    return True

  def __lt__(self, other):
    return True

  def __getitem__(self, index):
    return 0

class NonSearchy:
  def __lt__(self, other):
    return False

  def __gt__(self, other):
    return False

  def __bool__(self, other):
    return False

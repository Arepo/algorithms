import os
import sys
import inspect
import pdb
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from linked_list import SinglyLinkedList
from linked_list_node import LinkedListNode
from collections import deque
import pdb

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.layer = None

  def __str__(self):
    return "Node <{}>".format(self.data)

  def __repr__(self):
    return "Node <{}>".format(self.data)

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




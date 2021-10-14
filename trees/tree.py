import pdb

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    # self.traversal_record = []

  def __str__(self):
    return "Node <{}>".format(self.data)

  def __repr__(self):
    return "Node <{}>".format(self.data)

  def record_in_order_traversal(self, node, traversal_record):
    if node:
      node.record_in_order_traversal(node.left, traversal_record)
      traversal_record.append(node.data)
      node.record_in_order_traversal(node.right, traversal_record)

  def record_pre_order_traversal(self, node, traversal_record):
    if node:
      traversal_record.append(node.data)
      node.record_pre_order_traversal(node.left, traversal_record)
      node.record_pre_order_traversal(node.right, traversal_record)

  def record_post_order_traversal(self, node, traversal_record):
    if node:
      node.record_post_order_traversal(node.left, traversal_record)
      node.record_post_order_traversal(node.right, traversal_record)
      traversal_record.append(node.data)

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




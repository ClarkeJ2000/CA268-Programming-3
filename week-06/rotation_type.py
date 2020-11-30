def avl_rotation_type(bst):
  rtype = ""
  ptr = bst.root
   
  while ptr != None: 
      if ptr.left == None and ptr.right == None:
        return rtype
      if ptr.left == None:
        rtype += "r"
        ptr = ptr.right
      else:
        rtype += "l"
        ptr = ptr.left
  
  return rtype

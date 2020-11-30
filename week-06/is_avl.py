def is_avl(bst):
     if bst == None: 
         return True
     if abs(bst.r_height(bst.root.right) - bst.r_height(bst.root.left) ) > 1:
         return False
     return True

def r_height(self, ptr):
     if ptr == None:
        return 0
     else:
        return (self.r_height(ptr.left) - self.r_height(ptr.right))
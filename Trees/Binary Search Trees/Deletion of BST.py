class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def ConstructionBST(root,val) :
        if root==None:
            return TreeNode(val)    
        elif root.val > val:
            root.left=ConstructionBST(root.left,val)
        else:
            root.right=ConstructionBST(root.right,val)
        return root
def findInorderSuccessor(root):
        while root.left != None:
            root = root.left 
        return root.val
 
def deleteNode(root, val):
        if root == None:
            return None 
        elif root.val > val:
            root.left = deleteNode(root.left, val)
        elif root.val < val:
            root.right =deleteNode(root.right, val)
        else:
            if root.left == None and root.right == None:
                return None 
            elif root.left == None:
                return root.right 
            elif root.right == None:
                return root.left 
            else:
                successor = findInorderSuccessor(root.right)
                root.val = successor 
                root.right = deleteNode(root.right, successor)
        return root
def printing(root):
    if root==None:
        print(None)
    Q=[root]
    while len(Q)>0:
        n=Q.pop(0)
        print(n.val,end=" ")
        if n.left !=None:
            Q.append(n.left)
        if n.right!=None:
            Q.append(n.right)
    
ele=[10,4,2,6,43,8,20]
root=None
for i in ele:
    root=ConstructionBST(root,i)
printing(root)
print()
deleteNode(root,10)
printing(root)
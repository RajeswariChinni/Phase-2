class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def insertIntoBST(root,val) :
        if root==None:
            return TreeNode(val)    
        elif root.val >val:
            root.left=insertIntoBST(root.left,val)
        else:
            root.right=insertIntoBST(root.right,val)
        return root
def ConstructionBST(root,val) :
        if root==None:
            return TreeNode(val)    
        elif root.val > val:
            root.left=ConstructionBST(root.left,val)
        else:
            root.right=ConstructionBST(root.right,val)
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
insertIntoBST(root,56)
printing(root)
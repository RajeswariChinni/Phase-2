class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printingInorder(root):
    if root==None:
        return
    printingInorder(root.left)
    print(root.data,end=" ")
    printingInorder(root.right)
    
def printingpreorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    printingpreorder(root.left)
    printingpreorder(root.right)
def printingpostorder(root):
    if root==None:
        return
    printingpostorder(root.left)
    printingpostorder(root.right)
    print(root.data,end=" ")
def printingLevelorder(root):
    if root is None:
        return
    result=[]
    Q=[root]
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        for i in range(n):
            #step-1
            currNode=Q.pop(0)
            # step - 2
            subResult.append(currNode.data)
 
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
        result.append(subResult)
    print(result)

def printingZigzagLevelorder(root):
    if root is None:
        return
    result=[]
    Q=[root]
    level=0
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        for i in range(n):
            #step-1
            currNode=Q.pop(0)
            # step - 2
            subResult.append(currNode.data)
 
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
        if level%2==1:
            subResult=subResult[::-1]
        level+=1
        result.append(subResult)
    print(result)

obj1=Box(12)
obj2=Box(13)
obj3=Box(45)
obj4=Box(84)
obj5=Box(23)
obj6=Box(68)
obj7=Box(32)
obj8=Box(90)
obj9=Box(100)
obj1.left=obj3
obj1.right=obj2
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.left=obj8
obj4.right=obj9
printingInorder(obj1)
print()
printingpreorder(obj1)
print()
printingpostorder(obj1)
print()
printingLevelorder(obj1)
print()
printingZigzagLevelorder(obj1)
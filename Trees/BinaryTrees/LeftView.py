class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def LeftView(root):
    
    # code here
    if root is None:
        return []
    Q=[root]
    results=[]
    while len(Q)>0:
        n=len(Q)
        for i in range(n):
            curr=Q.pop(0)
            if i==0:
                results.append(curr.data)
            if curr.left !=None:
                Q.append(curr.left)
            if curr.right!=None:
                Q.append(curr.right)
    return results


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
print(LeftView(obj1))
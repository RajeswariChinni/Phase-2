
class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def topViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]
 
    topViewHelper(root.left, store, hd - 1, level + 1)
    topViewHelper(root.right, store, hd + 1, level + 1)
 
def findTopView(root):
    result = []
    if root == None:
        return result
 
    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result

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
print(findTopView(obj1))
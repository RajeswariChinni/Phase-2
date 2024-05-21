# str=input()
# vow=['a','e','i','o','u','A','E','I','O','U']
# count=0
# for i in str:
#     if i in vow:
#         count+=1
# print(count)


# str2='likhitaa'
# strr=sorted(str2)
# re={}
# for i in strr:
#     if i in re:
#         re[i]+=1
#     else:
#         re[i]=1
# k=list(re.keys())
# v=list(re.values())
# print(k[v.index(max(v))])   

# str2 = 'likhitaa'
# re = {}
# max_count = 0
# max_char = None

# for char in str2:
#     if char in re:
#         re[char] += 1
#     else:
#         re[char] = 1
    
#     if re[char] > max_count:
#         max_count = re[char]
#         max_char = char
#     elif re[char] == max_count:
#         if max_char is None or char < max_char:
#             max_char = char

# print(max_char)

# word = input()
# store = {}
# for ch in word:
#     if ch in store:
#         store[ch] += 1 
#     else:
#         store[ch] = 1 
 
# print(store)
# print(store.keys())
 
# resultChar = ''
# resultFreq = 0
# for key in store.keys():
#     if resultFreq < store[key]:
#         resultFreq = store[key]
#         resultChar = key 
#     elif resultFreq == store[key] and ord(key) < ord(resultChar):
#         resultChar = key
 
# print(resultChar)

class Box:
    def __init__(self,data) -> None:
        self.data=data 
        self.next=None
    
def printLinked(curr):
        while curr!=None:
         print(curr.data)
         curr=curr.next 
def insertattail(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    tail=head
    while tail.next !=None:
        tail=tail.next
    tail.next=temp
    return head
def insertatbeginning(head,ele):
    temp=Box(ele)
    if head== None:
        return temp
    temp.next =head
    return temp
def insertatspecific(head,pos,ele):
    if pos==0:
        insertatbeginning(head,ele)
    temp=Box(ele)
    currindex=0
    currnode=head
    while currindex!=pos-1:
        currindex+=1
        currnode=currnode.next 
    temp.next=currnode.next
    currnode.next = temp
    return head
#block creation is happening in below 3 lines
obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
#establishing links in below 3 lines
obj1.next=obj2
obj2.next=obj3
obj3.next=None
insertattail(obj1,4)
k=insertatbeginning(obj1,1)
insertatspecific(k,3,3)
printLinked(k)
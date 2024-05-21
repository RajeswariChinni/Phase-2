class Box:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
def insertattail(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=temp
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
def printing(head):
    curr=head
    while curr!=None:
        if(curr.next!=None): 
            print(curr.data ,end="-->")
        else:
            print(curr.data,end="-->None")
        curr=curr.next
    print()
def deletingattail(head):
    if head==None or head.next==None:
        return None
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head
def deletingatbeginning(head):
    if head==None or head.next==None:
        return None
    second=head.next
    head.next=None
    return second
def deletingatspecific(head,pos):
    if pos==0:
        deletingatbeginning(head)
    index=0
    node=head
    while index!=pos-1:
        index+=1
        if node.next==None:
            raise Exception( "Not Vaild Position Entered")
        node=node.next
    if node.next==None:
        raise Exception("Not Vaild Position Entered")
    temp=node.next
    node.next=temp.next
    temp.next=None
n=[1,2,3,4,5,6,7,8,9]
head=None
for i in n:
    head=insertattail(head,i)
printing(head)
head=deletingattail(head)
printing(head)
head=deletingatbeginning(head)
printing(head)
pos=3
deletingatspecific(head,pos)
printing(head)
insertattail(head,4)
head=insertatbeginning(head,1)
insertatspecific(head,3,3)
printing(head)
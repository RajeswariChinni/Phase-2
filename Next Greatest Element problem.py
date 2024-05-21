# # Find the next greater element ?
# # Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
# # Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
# # If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

def findNextGreaterElement(arr):
    n=len(arr)
    l=[-1]*n
    for i in range(n-1):
        j=i+1
        while (j!=n):
            if arr[i]<arr[j] :
                l[i]=arr[j]
                break
            else:
                j+=1
    return l
        
#     stack=[]
#     n=len(nums)
#     res=[-1]*n
    
#     for i in range(n-1,-1,-1):
#         while len(stack)>0 and stack[0]<nums[i]:
#             stack.pop(0)
#         if len(stack) >0:
#             res[i]=stack[0]
#         stack.insert(0,nums[i])
#     return res
            
nums=[1,3,2,4]
print(findNextGreaterElement(nums))

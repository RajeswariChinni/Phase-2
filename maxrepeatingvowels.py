#counting the characters 
# str=input()
# vow=['a','e','i','o','u','A','E','I','O','U']
# count=0
# for i in str:
#     if i in vow:
#         count+=1
# print(count)

# #anthoer method
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

# #same method different style
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

#print(max_char)

word = input()
store = {}
for ch in word:
    if ch in store:
        store[ch] += 1 
    else:
        store[ch] = 1 
 
print(store)
print(store.keys())
 
resultChar = ''
resultFreq = 0
for key in store.keys():
    if resultFreq < store[key]:
        resultFreq = store[key]
        resultChar = key 
    elif resultFreq == store[key] and ord(key) < ord(resultChar):
        resultChar = key
 
print(resultChar)
List = [1000,2,2,4,50,6,7,8,9,10]
k = 1
sublist = []
s = 0
def remaining(List,k,s):
    n = List.__len__()
    while(s < n):
        a = List[s]
        sublist.append(a)
        s = s + (k+1)
    print(List)
   # print(sublist)
    for i in List:
        if i in sublist:
            List.remove(i)
    print(List)
    if (List.__len__() <= k and List.__len__() >= 1):
        for i in List:
            List.pop()
        #print(List)

    if List.__len__()>k :
        s=0
        sublist.clear()
        remaining(List, k, s)
remaining(List,k,s)

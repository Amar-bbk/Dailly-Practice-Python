def MaxAreaContainer(arr):
    n = arr.__len__()

    maxArea = 0
    for i in range(0, n):
        for j in range(i+1,n):
            ContHeight = min(arr[i],arr[j])
            ContWidth = abs(j - i)
            ContArea = ContHeight * ContWidth
            if (ContArea > maxArea):
                maxArea = ContArea
    return maxArea

Array = [3,7,9,8,0,0]
print("The maximum area of container is : ",  MaxAreaContainer(Array))
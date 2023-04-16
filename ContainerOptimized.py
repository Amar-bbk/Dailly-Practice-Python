def ContainerOptimized(arr):
    n = arr.__len__()
    maxArea = 0
    i = 0
    j = n-1
    while(i < j):
        ContHeight = min(arr[i],arr[j])
        ContWidth = abs(i-j)
        ContArea = ContHeight * ContWidth
        if ContArea > maxArea:
            maxArea = ContArea
        if arr[i] <= arr[j]:
            i = i + 1
        elif arr[j] <= arr[i]:
            j = j - 1;
    return maxArea
arr = [1,3,9,5,2,1]
print("Tha max area of container is : ", ContainerOptimized(arr))
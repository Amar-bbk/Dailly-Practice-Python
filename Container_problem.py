def ContainersArea(arr):
    maxArea = 0
    n = arr.__len__()
    if n <= 1:
        return None
    if n > 1:
        for i in range(0,n):
            for j in range(i+1,n):
                if(arr[i] > arr[j]):
                    length = arr[j]
                elif(arr[i] < arr[j]):
                    length = arr[i]
                else:
                    length = arr[i]
                width = abs(i-j)
                Area = length * width

                if (maxArea < Area):
                    maxArea = Area

    return maxArea

array = [7,23,3,50,9,1]
print('The max area of Container is :', ContainersArea(array))

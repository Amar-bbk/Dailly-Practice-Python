#Container with most water program
def AreasOfWater(arr):
    area = []
    length = 0
    width = 0
    n = arr.__len__()
    if n<=1:
        return None;
    if n > 1:
        for i in range(0,n):  
            for j in range(i+1, n):
                if(arr[i] > arr[j]):
                    length = arr[j]
                elif(arr[i] < arr[j]):
                    length = arr[i]
                else:
                    length = arr[i]
                width = abs(i-j)
                area.append(length*width)
        return area
array = [6,9,3,4,5,8]

if AreasOfWater(array) is None:
    print('Container is NOT present in this list')
else:
    print('Areas of containers are : ',AreasOfWater(array))
    print('Area of container that would hold greatest amount of water is : ',max(AreasOfWater(array)))

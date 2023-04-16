# A = [2,5,9,10,12]
# x = 0
# y = 0
# for i in range(0,A.__len__()):
#     for j in range(i+1, A.__len__()):
#         if(A[i] + A[j] == 19):
#             x = A[i]
#             y = A[j]
#             print(x, y)
#             break
# if (x + y) != 19:
#     print('Those two numbers are not present  in this array whose sum is  19')
# Python program to find two numbers X,Y from a given list whose sum is Y
X = None
Y = None
def TwoNumsWhoseSumIs(arr, sum):
    global X
    global Y
    for i in range(0, arr.__len__()):
        for j in range(i + 1, arr.__len__()):
            if arr[i] + arr[j] == sum:
                X = arr[i]
                Y = arr[j]
                break
    if (X != None and Y != None):
        print("Two numbers whose sum is 5 are:", X, Y)
    else:
        print('The two numbers not found in the list whose sum is:  ', sum)



a = [0, 0, 3, 5, 10, 100, 210, 139]
sum = 5
TwoNumsWhoseSumIs(a, sum)

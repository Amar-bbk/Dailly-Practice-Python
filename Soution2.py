def TwoNumsWhoseSumIs(arr, sum):
    M = False
    for i in range(0, arr.__len__()):
        for j in range(i + 1, arr.__len__()):
            if arr[i] + arr[j] == sum:
                print("Two numbers whose sum is 5 are:", arr[i], arr[j])
                M = True
                break
    if (M == False):
        print('The two numbers not found in the list whose sum is:  ', sum)

a = [0, 0, 3, 5, 10, 100, 210, 139]
sum = 2345
TwoNumsWhoseSumIs(a, sum)
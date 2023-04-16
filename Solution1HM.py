def TwoNumsWhoseSumIs(arr, sum):
    HM1  = {}
    notfound = False
    for i in range(0,arr.__len__()):
        q = sum - arr[i]
        if q in HM1:
            print(q , arr[i])
            notfound = False
            break
        else:
            HM1[arr[i]] = i
            notfound = True
    if notfound == True:
        print("Numbers not found")
    print(HM1)


#a = [0, 0, -3, 5, 10, 100, 210, 139]
a = [6,6,10]
sum = 12
TwoNumsWhoseSumIs(a, sum)

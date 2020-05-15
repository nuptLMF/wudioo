
ss = []
arr = [4,2,1,0,1,2,3,4,0,5,7,8,6]
new_arr = arr
if 0 in arr:
    num = 0
    for i in arr:
        if i ==0:
            num = new_arr.index(i)
            new_arr = new_arr[num+1:]
            print(new_arr)
            ss.append(num)
print(ss)
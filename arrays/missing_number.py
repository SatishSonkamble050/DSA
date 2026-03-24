# 

def brute(arr):
    n = len(arr)
    if n <= 0:
        return "empity arr"
    arr.sort()
    sum = None
    number = None
    for index, num in enumerate(arr):
        if index < len(arr):
            sum = arr[index+1] - num
            number = num
            if sum != 1:
                return num+1

    # if sum != 1:
    #     for i

arr = [9,6,4,2,3,5,7,0,1]
print(f"ARR : ", brute(arr))


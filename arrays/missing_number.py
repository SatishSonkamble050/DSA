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
# print(f"ARR : ", brute(arr))


def optimal(arr):
    n = len(arr)
    xor1 = 0
    xor2 = 0

    for i in range(n + 1):
        print(f"{i} and  : {xor1}")
        xor1 ^= i

    for num in arr:
        xor2 ^= num
    
    print(f"01 : {xor1} --- 02 : {xor2}")

    return xor1 ^ xor2


arr = [9,6,4,2,5,7,0,1]
print("Optimal:", optimal(arr))

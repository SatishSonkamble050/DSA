# 

def brute(arr):
    n = len(arr)
    majority_count = n/2
    haspmap = {}
    for i in arr:
        if i in haspmap:
            haspmap[i] +=1
        else:
            haspmap[i] = 1

    for i in haspmap:
        if haspmap[i] >= majority_count:
            return i
        
    return "No"

arr = [3,2,3]
print("RESULT  : ", brute(arr))


def optimize(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

arr = [3,2,3]
print("RESULT  : ", optimize(arr))
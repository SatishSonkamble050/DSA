
def prefex(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i-1]+arr[i]

    return arr

def find_midian(pre):
    mid = len(pre)//2
    end = pre[len(pre)-1]
    left = pre[mid-1]
    right = end - pre[mid+1]
    print (f"MID : {mid} -- LEFT : {left} --- RIGHT : {right} --- END : {end} --- LENGTH : {len(pre)}")

    while mid !=0 and mid != len(pre)-1:
        print(f"Left : {left} -- Right : {right} ---- MID : {pre[mid]} ---- MID INDEX : {mid} ")
        if left == right:
            return mid

        if left < right:
            mid =mid+1
        else:
            mid = mid-1
        left = pre[mid-1]
        right = end - pre[mid+1]

arr = [10,20,30,5,60]
result = prefex(arr)
final_result = find_midian(result)

print("ARRAY :", result, final_result )








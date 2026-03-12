def dynamic_sliding_window(arr):
    memory = []
    max_len = 0
    for i in range(len(arr)):
        if len(memory) > 0:
            for j in range(len(memory)):
                if memory[j] == arr[i]:
                    # for k in range(j, len(memory)):
                    #     memory.remove(memory["k"])
                    memory = memory[j+1:]
                    break
                
        
        memory.append(arr[i])
        if max_len < len(memory):
            max_len = len(memory)

    return max_len


arr = "abcadbcae"

result  = dynamic_sliding_window(arr)
print("result : ", result)
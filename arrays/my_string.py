def string_check(s, arr):
    total_count = 0
    for arr_string in arr:
        index = 0
        count = 0
        print(f"SRRAY STRING :  {arr_string}")
        for char in arr_string:
            print(f"CHAR MAIN : {char}")
            for c in range(index,len(s)):
                print(f"char : {char} ----  string Char : {s[c]} : index : {c}")
                if char == s[c]:
                    count +=1
                    index = c+1
                    break
        print(f"count : {count} --- len : {len(arr_string)}")
        if count == len(arr_string):
            total_count +=1
    return total_count


s = "abcde"
arr = ["a", "bb", "acd", "ace"]

print("REsult :", string_check(s, arr))
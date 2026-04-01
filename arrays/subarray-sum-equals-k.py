# -----------------------------------------
# Subarray Sum Equals K
# -----------------------------------------

# 1️⃣ Brute Force Approach (O(n^2))
def brute(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1

    return count


# 2️⃣ Optimal Approach (Prefix Sum + HashMap) → O(n)
def optimal(nums, k):
    prefix_map = {0: 1}  # base case
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        # check if (current_sum - k) exists
        if current_sum - k in prefix_map:
            count += prefix_map[current_sum - k]

        # update hashmap
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    return count


# -----------------------------------------
# 🔥 Main Function (Testing)
# -----------------------------------------
if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3

    print("Input:", nums, "k =", k)
    print("Brute Force Result:", brute(nums, k))
    print("Optimal Approach Result:", optimal(nums, k))


# -----------------------------------------
# 🧠 Notes:
# -----------------------------------------
# - Brute → O(n^2)
# - Optimal → O(n)
# - Sliding Window ❌ (not valid for negative numbers)
# -----------------------------------------
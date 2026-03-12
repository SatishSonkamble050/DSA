You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes. 

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.


Steps 
1. one loop i and other inner loop j 
2. i+j == target then inc the count

optimize
1. two pointer
2. if p1 + p2 == target move count++ p2--
3. if p1+p2 > target move p2--
4. if p1+p2 < target move p1++

Prblem 2 : @@@@@@@@@@@@
2. Best Time to Buy and Sell Stock

BruteForce

1. i start from 0 and j start from i+1
2. arr[j] - arr[i] > max_profit strore new one

better:

5, 6, 3, 4, 6, 2, 4

5-6, 3, 4, 6, 2, 4
6-3, 4, 6, 2, 4

p1 = 5
p2 = 6

p2-p1 = 1
max = 1 

if p1 < p2
    p1= p2
    p2++
else
p2++



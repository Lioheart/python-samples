"""Maximum Subarray Problem"""
def max_sequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans


print(max_sequence([]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([-2, 1]))
print(max_sequence([ 17, -31, 3, 23, 5, 19, -27, -42, -25, -26, -21, 2, 43, -5, 23 ]))
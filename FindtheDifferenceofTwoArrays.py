# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

def arrayDiff(nums1,nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    resnum1, resnum2 = [], []
    for num in nums1:
        if num not in nums2:
            resnum1.append(num)
    for num in nums2:
        if num not in nums1:
            resnum2.append(num)
    return [resnum1, resnum2]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(arrayDiff(nums1,nums2))  
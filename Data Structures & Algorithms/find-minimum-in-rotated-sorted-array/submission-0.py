class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # default value of min num
        l, r = 0, len(nums) - 1

        while l <= r:
            # if the arr is sorted the left is the min val
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                # search in the right
                l = mid + 1
            else:
                # search in the left
                r = mid - 1

        return res
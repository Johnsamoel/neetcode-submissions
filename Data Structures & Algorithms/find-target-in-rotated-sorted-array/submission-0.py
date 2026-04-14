class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            
            # left half is sorted and we're in it
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            # right half is sorted and we're in it
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
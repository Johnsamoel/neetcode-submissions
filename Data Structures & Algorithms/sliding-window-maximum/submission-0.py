class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # index
        output = []
        l = r = 0

        while r < len(nums):
            # check the max val in queue before adding the curr num
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # pop the left of queue in case it is not in bound
            if q[0] < l:
                q.popleft()

            # update the max if window reached k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l+= 1
            r+=1

        return output
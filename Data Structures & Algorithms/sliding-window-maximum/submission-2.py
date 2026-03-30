class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # we storing indicies
        res = []
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            #if the index at the front is < l, then its out of bounds no longer in current window
            if q[0] < l:
                q.popleft()
            # window slides by 1 each time, since arrays are 0 indexed first window is when r + 1 = k,
            # after that each window slides by 1 so thats why ts works 
            if (r + 1) >= k:
                i = q[0]
                res.append(nums[i])
                l += 1

        return res
               
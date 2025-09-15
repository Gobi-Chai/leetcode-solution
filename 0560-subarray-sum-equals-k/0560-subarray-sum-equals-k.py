from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        consider pre[i] as the sum of sums[0,...,i] 
        WTS pre[j] - pre[i-1] = k, which is pre[i-1] = pre[j] - k
        we need to iterate the how many times we have got pre[j] - k
    
        """
        total = 0 # current prefix sum
        ans = 0 # nums of subarrays
        cnt = defaultdict(int)
        cnt[0] = 1

        for x in nums:
            total += x
            need = total - k
            if need in cnt:
                ans += cnt[need]
            cnt[total] += 1
        return ans
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        consider pre[i] as the sum of sums[0,...,i] 
        WTS pre[j] - pre[i-1] = k, which is pre[i-1] = pre[j] - k
        we need to iterate the how many times we have got pre[j] - k
    
        """

        total = 0 # current prefix sum
        ans = 0 # numbers of subarrays
        cnt = {0:1}

        for x in nums:
            total += x 
            need = total - k    
            if need in cnt:
                ans += cnt[need]

            cnt[total] = cnt.get(total, 0) + 1

        return ans


        
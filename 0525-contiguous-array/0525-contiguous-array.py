class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Treat 0 as -1 and calculate the sum of the prefix
        count = 0 
        first_occurrence = {0: -1}
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else: 
                count += 1
            
            # if the count has occurred before, then the mid section sums up to 0
            if count in first_occurrence:
                max_len = max(max_len, i - first_occurrence[count])
            else:
                first_occurrence[count] = i

        return max_len
        
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater_map = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater_map[prev] = num
            stack.append(num)

        
        return [next_greater_map.get(x, -1) for x in nums1]
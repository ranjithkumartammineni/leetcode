#945. Minimum Increment to Make Array Unique
#python

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                inc=nums[i-1]-nums[i]+1
                nums[i]=inc+nums[i]
                moves=moves+inc
        return moves

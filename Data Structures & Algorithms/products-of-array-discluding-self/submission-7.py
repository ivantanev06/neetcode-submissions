class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = [0] * len(nums)
        zeros_index = []
        for index, val in enumerate(nums):
            if val == 0:
                zeros_index.append(index)
            else:
                continue
        
        if len(zeros_index) == 0:
            N = 1
            for val in nums:
                N = N*val
            for i in range(len(nums)):
                return_list[i] = N // nums[i]
            

        elif len(zeros_index) == 1:
            N = 1
            for i in range(len(nums)):
                if i != zeros_index[0]:
                    N = N * nums[i]
            return_list[zeros_index[0]] = N
        
        return return_list
                


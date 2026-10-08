class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for index, num in enumerate(nums):
            needed = target - num

            if needed in counts:
                i = min(index, counts[needed])
                j = max(index, counts[needed])
                return ([i,j])
            else:
                counts[num] = index
                continue

        return False
        
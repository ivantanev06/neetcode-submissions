class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        return_list = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        sorted_counts = dict(sorted(counts.items(), key = lambda item : item[1], reverse = True))
        for i in range(k):
            return_list.append(list(sorted_counts.keys())[i])
        return return_list



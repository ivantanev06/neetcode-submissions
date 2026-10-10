class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        return_list = []
        #Go through the list of numbers and count 
        #how many times each one occurs
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        #Create n+1 buckets where freq[i] are all numbers
        #which appeared i times.
        #the frequency of any number <= len(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in zip(list(counts.keys()), list(counts.values())):
            freq[count].append(num)
        
        #Now iterate through freq backwards and return the first 
        #k numbers we encounter

        for r in range(len(nums), -1, -1):
            if len(return_list) == k:
                return return_list
            else:
                if len(freq[r]) != 0:
                    return_list.extend(freq[r])




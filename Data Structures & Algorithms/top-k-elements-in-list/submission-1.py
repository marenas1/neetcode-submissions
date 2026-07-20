class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answers = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        maximum = 0
        for num in freq:
            if freq[num]>maximum:
                maximum=freq[num]
        print(maximum)    
        while len(answers)!=k:
            for num in freq:
                if (num not in answers) and (freq[num]==maximum):
                    answers.append(num)
            maximum-=1
        return answers
        
        
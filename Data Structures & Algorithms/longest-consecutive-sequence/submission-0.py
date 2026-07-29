class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mynums = set(nums)
        print(nums)
        longest = 0
        for num in mynums:
            currentLongest = 0
            if num-1 not in mynums:
                #meaning its the start of a sequence
                #check how long it goes on
                currentLongest = 1
                nextNum = num+1
                while nextNum in mynums:
                    currentLongest+=1
                    nextNum+=1
                longest =  max(longest,currentLongest)

        return longest
        
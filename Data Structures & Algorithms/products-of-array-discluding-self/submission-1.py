class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums) 
        suffix = [0] * len(nums)
        answers = []
        for i in range(len(nums)):
            if i==0:
                prefix[0]=nums[i]
            else:
                prefix[i]=nums[i]*prefix[i-1]

        print(prefix)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                suffix[i]=nums[i]
            else:
                suffix[i]=nums[i]*suffix[i+1]
        print(suffix)

        for i in range(len(nums)):
            if i == 0:
                left_product = 1
            else:
                left_product = prefix[i - 1]

            if i == len(nums) - 1:
                right_product = 1
            else:
                right_product = suffix[i + 1]

            answers.append(left_product * right_product)
        return answers
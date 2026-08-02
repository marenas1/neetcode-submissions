class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r= len(heights)-1
        area = min(heights[l],heights[r])*(r-l)
        print(area)
        while l<r:
            difference = r-l
            currArea = min(heights[l],heights[r])*difference
            print(currArea)
            if currArea > area:
                area = currArea
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return area
            

        
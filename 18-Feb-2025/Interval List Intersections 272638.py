# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # diff = [0] *1000
        output = []
        # for A in firstList:
        #     l,r = A
        #     diff[l] += 1
        #     diff[r+1] -= 1
        # for B in secondList:
        #     l,r = B
        #     diff[l] += 1
        #     diff[r+1] -= 1
        # for i in range(1,len(diff)):
        #     diff[i] += diff[i-1]
        # start = -1
        # inside = False   

        # for i in range(len(diff)):
        #     if diff[i] >= 2:   
        #         if not inside:
        #             start = i  # Start of the intersection
        #             inside = True
        #     elif inside:  # Overlapping region ends
        #         output.append([start, i - 1])
        #         inside = False  # Reset flag
        
        # return output
        # i = 0
        # j = 0
        # output = []
        # for A in firstList:

        #     start1,end1 = A
        # for B in secondList:
        #     start2,end2 = B
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            start1,end1 = firstList[i]
            start2,end2 = secondList[j]

            start = max(start1,start2)
            end = min(end1,end2)

            if start <= end:
                output.append(([start,end]))
            if end1 < end2:
                i += 1
            else:
                j += 1
        return output 

           


        

        


        print(diff)
       
        
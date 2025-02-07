# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        output = []
        for i in range(len(img)):
            output.append([0]*len(img[0]))
         
        for row in range(len(img)):
            for col in range(len(img[row])):
                possibility = [[row - 1,col -1],[row-1,col],[row-1,col+1],[row,col-1],[row,col],[row,col+1],[row+1,col-1],[row + 1,col],[row+1,col+1]]
                summ = 0
                count = 0
                for poss in possibility:
                    if 0 <= poss[0] < len(img) and 0 <= poss[1] < len(img[row]):
                        summ += img[poss[0]][poss[1]]
                        count += 1
                if count != 0:
                    summ = summ//count
                output[row][col] = summ
        return output


                

      

        # for row in range(len(img)):
        #     for col in range(len(img[0]):
        #         smooth_ave = 0
        #         _sum = []
        #         for i in range(3):
        #             for j in range(3)
        #         for img[i][j] in img:
        #             valid = 0



         
        
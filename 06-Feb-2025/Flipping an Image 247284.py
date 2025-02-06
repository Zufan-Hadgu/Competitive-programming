# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_img = []
        for img in image:
            new_img.append(img[::-1])
        print(new_img)

        for nimg in new_img:
            for j in range(len(nimg)):
                if nimg[j] ==1:
                    nimg[j] =0
                elif nimg[j] == 0:
                    nimg[j] = 1
        return new_img



       
        
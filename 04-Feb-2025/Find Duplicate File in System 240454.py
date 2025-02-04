# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        new_dict = {}
        arrValues = []
        for i in range(len(paths)):
            new_array = paths[i].split(" ")
           
            dirr = new_array[0]
            n = len(new_array)
            for j in range(1,n):
                k = len(new_array[j])-1
                ind = new_array[j].index('(')
                content = new_array[j][ind + 1:k]
                filepath = dirr + '/' + new_array[j][:ind]
                new_dict[filepath] = content
                arrValues.append(content)

        # print(new_dict)
        countedDict = Counter(arrValues)
        print(countedDict)
        result = []
        for values in countedDict:
            if countedDict[values] > 1:
                last_arr = [path for path,val in new_dict.items() if new_dict[path] == values ]
                result.append(last_arr)
            last_arr = []
        return result




                










       




        
        
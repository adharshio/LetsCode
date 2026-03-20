import numpy as np
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area=0
        max_diagonal=0
        max_areaList=[]
        max_diagonalList=[]
        max_final=[]
        for i in range(len(dimensions)):
            length=dimensions[i][0]
            width=dimensions[i][1]
            diagonal=float(np.sqrt(length**2 + width**2))
            max_area=length*width
            max_areaList.append(max_area)
            max_diagonalList.append(diagonal)
        max_digVal= max(max_diagonalList)
        max_digValIndex=max_diagonalList.index(max_digVal) 
        max_areaVal=max(max_areaList)
        for i in range(len(max_areaList)):
            if max_diagonalList.count(max_digVal)==1:
                return max_areaList[max_digValIndex]
                
            else:
                for i in range(len(max_diagonalList)):
                    if max_diagonalList[i]==max_digVal:
                        max_final.append(i)

        max_final1=0
        for i in max_final:
            max_final1=max(max_areaList[i],max_final1)

        return max_final1
        #one of the hardest interesting question

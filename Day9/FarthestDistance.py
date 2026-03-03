class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_max=0
        right_max=0
        Lstring=moves.replace("_","L")
        Rstring=moves.replace("_","R")
        for i in Lstring:
            if i=="L":
                left_max+=1
            else:
                 left_max-=1
        for i in Rstring:
            if i=="R":
                right_max+=1
            else:
                right_max-=1
        return max(left_max,right_max)
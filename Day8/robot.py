class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hor=0
        ver=0
        for i in moves:
            if i=="U":
                ver+=1
            elif i=="D":
                ver-=1
            elif i=="R":
                hor+=1
            else:
                hor-=1
        if ver==0 and hor==0:
            return True
        else:
            return False
        

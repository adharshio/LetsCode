  answer=0
        n=len(s)
        max_val=float('-inf') 
        for i in range(n):
             
            answer=s[:i].count("(")-s[:i].count(")")
            max_val=max(answer,max_val)
        return max_val
         
class Solution:
    def interpret(self, command: str) -> str:
        answer=""
        n=len(command)
        for i in range(n):
            if command[i]=="G":
                answer+="G"
            elif command[i]=="(" and command[i+1]=="a":
                answer+="al"
            elif command[i]=="(" and command[i+1]==")":
                answer+="o"
        return answer

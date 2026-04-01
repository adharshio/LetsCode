class Solution:
    def capitalizeTitle(self, title: str) -> str:
        strings=title.split()
        n=len(strings)
        new_str=""
        for i in range(n):
            if len(strings[i])>2:
                new_str+=strings[i].capitalize()
            else:
                new_str+=strings[i].lower()
            if i!=n-1:
                new_str+=" "
        return new_str

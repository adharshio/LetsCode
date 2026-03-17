class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newStr=""
        # for index in indices:
        #     newStr+=s[index]
        # return newStr
        dict1=dict(zip(indices,s))
        # print(dict1)
        # sorted_dict=dict(sorted(dict1.items(),key=lambda item: item[1]))
        sorted_dict=dict(sorted(dict1.items()))
        for i in sorted_dict:
            newStr+=sorted_dict[i]
        return newStr

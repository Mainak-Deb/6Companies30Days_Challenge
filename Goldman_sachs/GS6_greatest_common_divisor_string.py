class Solution:    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1),len(str2))):
            if(str1[i]!=str2[i]):return ""
        while(str2!=""):
            mod=str1.replace(str2,"")
            if((len(str1)>=len(str2)) and (mod==str1)):return ""
            else:str1,str2=str2,mod
        return str1
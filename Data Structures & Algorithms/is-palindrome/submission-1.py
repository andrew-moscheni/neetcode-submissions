class Solution:
    def isPalindrome(self, s: str) -> bool:
        #preprocess string FIRST
        new_str=""
        for i in s:
            i=i.lower()
            if i.isalnum():
                new_str=new_str+i
        left, right=0,len(new_str)-1
        while left<=right:
            if new_str[left]!=new_str[right]:
                return False
            left+=1
            right-=1
        return True
        
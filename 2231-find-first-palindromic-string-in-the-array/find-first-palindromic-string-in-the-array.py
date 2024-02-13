class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word[0]==word[len(word)-1]:
                if word[0:len(word)]==word[::-1]:
                    return word
                    break;
        
        return ""
        
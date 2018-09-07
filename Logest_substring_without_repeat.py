'''
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
Input: "aab"
Output: 2

Input: "dvdj"
Output: 3

'''

def lengthOfLongestSubstring(self, s):
        num1 = num2 = 0
        for cnt1 in range(len(s)):

                sum = s[cnt1]
    

                for cnt2 in range(1, len(s) - cnt1):
                    if s[cnt1 + cnt2] not in sum:
                        sum += s[cnt1 + cnt2]
                    else:
                         break

                num2 = len(sum)
                
                if num2 > num1:
                    num1 = num2

        return(num1)
        

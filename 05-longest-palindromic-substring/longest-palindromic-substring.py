class Solution:
    ## bf approach
    # def longestPalindrome(self, s: str) -> int:
    #     longest = 0
    #     temp_str = ""
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             if j-i+1 < longest:
    #                 continue
    #             panlin = s[i:j+1]
    #             if panlin == panlin[::-1]:
    #                 if (j-i+1) > longest:
    #                     temp_str = s[i:j+1]
    #                     longest = j-i+1
    #     return temp_str

    ## centered approach
    # def longestPalindrome(self, s):
    #     if len(s)==0:
    #         return 0
    #     maxLen=1
    #     start=0
    #     for i in range(len(s)):
    #         print(i, i - maxLen)
    #         if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
    #             print("len 3 checked")
    #             start=i-maxLen-1
    #             maxLen+=2
    #             continue

    #         if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
    #             print("len 2 checked", s[i-maxLen:i+1])
    #             start=i-maxLen
    #             maxLen+=1
    #     return s[start:start+maxLen]

    ##Manacher algorithm
    ##http://en.wikipedia.org/wiki/Longest_palindromic_substring
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]


    ## dp approach
    # def longestPalindrome(self, s):
    #     n = len(s)
    #     dp = [[False for x in range(n)] for y in range(n)]
        
    #     start = 0
    #     longest = 1
    #     for i in range(n):
    #         dp[i][i] = True
        
    #     for l in range(2, n+1): # length from 2 to n
    #         for i in range(n-l+1):
    #             end = i+l
    #             if l == 2:
    #                 if s[i] == s[end-1]:
    #                     dp[i][end-1] = True
    #                     longest = l
    #                     start = i
    #             else:
    #                 if s[i] == s[end-1] and dp[i+1][end-2]:
    #                     dp[i][end-1] = True
    #                     longest = l
    #                     start = i 

    #     return s[start:start+longest]


tests = [
    (
        ("abbcb",),
        "bcb",
    ),
    (
        ("aaaaa",),
        "aaaaa",
    ),
    (
        ("babad",),
        "bab", 
    ),
    (
        ("cbbd",),
        "bb",
    ),
    (
        ("a",),
        "a",
    ),
]
# "uhrfjotnewtodhmbplsaolnpcdaohiytmfllukijouxipvqohtsgxbtfoxyfkfczkfwhzimbefiohmtimrcxbpgcxogystdkcqujvbxsgirpccdnvejtljftwkdpsqpflzwruwwdzovsbmwbcvlftkjnxqaguvtsycylqzquqkbnybnbaeahbxejhphwrpmymcemuhljwtuvxefqfzjhskuqhifydkxpnfwfxkpeexnjltfqwfvchphmtsrsyayxukvmlqodshqwbeaxhcxdbssnrdzvxtusngwqdxvluauphmmbwmgtazjwvolenegwbmjfwprfuswamyvgrgshqocnhirgyakbkkggviorawadzhjipjjgiwpelwxvtaegauerbwpalofrbghfhnublttqtcmqskcocwwwxpnckrnbepusjyohsrretrqyvgnbezuvwmzizcefxyumtdwnqjkgsktyuacfpnqocqjxcurmipjfqmjqrkdeqsfseyigqlwmzgqhivbqalcxhlzgtsfjbdbfqiedogrqasgmimifdexbjjpfusxsypxobxjtcwxnkpgkdpgskgkvezkriixpxkkattyplnpdbdifforxozfngmlgcunbnubzamgkkfbswuqfqrvzjqmlfqxeqpjaqayodtetsecmfbplscmslpqiyhhykftzkkhshxqvdwmwowokpluwyvavwvofwqtdilwqjgrprukzyhckuspyzaoe"
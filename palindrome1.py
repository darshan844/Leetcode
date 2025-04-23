class Solution:
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd_pal = expand_around_center(i, i)
            # Even-length palindrome
            even_pal = expand_around_center(i, i + 1)

            # Update longest palindrome
            if len(odd_pal) > len(longest):
                longest = odd_pal
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest

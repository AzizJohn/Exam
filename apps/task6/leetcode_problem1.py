class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for letter in s[::-1]:
            if letter == " ":
                if count >= 1:
                    return count
            else:
                count += 1
        return count

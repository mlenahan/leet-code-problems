# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.

def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balanced = 0
        count = 0
        for character in s:
            if character == 'L': 
                count += 1
            else: 
                count -= 1
            if count == 0 :
                balanced += 1
        return balanced
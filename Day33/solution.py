class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        
        # Find the first non-9 digit for max value
        max_digit = None
        for c in s:
            if c != '9':
                max_digit = c
                break
        if max_digit is None:
            max_num = num
        else:
            max_num = int(s.replace(max_digit, '9'))
        
        # Find the first non-0 digit for min value
        min_digit = None
        for c in s:
            if c != '0':
                min_digit = c
                break
        if min_digit is None:
            min_num = num
        else:
            min_num = int(s.replace(min_digit, '0'))
        
        return max_num - min_num
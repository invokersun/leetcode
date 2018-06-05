class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        if digits[-1]==9:
            res = self.plusOne(digits[:-1])
            res.append(0)
            return res
        else:
            digits[-1] += 1
            return digits
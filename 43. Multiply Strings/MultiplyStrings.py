class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        size1 = len(num1);size2 = len(num2)
        if size1 <= 5 and size2 <= 5:
            tmp = int(num1) * int(num2)
            return str(tmp)
        num1 = num1[::-1];num2 = num2[::-1]
        array = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                array[i + j] += int(num1[i]) * int(num2[j])
        ans = []
        for i in range(len(array)):
            digit = array[i] % 10
            carry = array[i] / 10
            if i < len(array) - 1:
                array[i + 1] += carry
            ans.insert(0,str(digit))
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        return ''.join(ans)
x = Solution()
print x.multiply("123456789", "987654321")
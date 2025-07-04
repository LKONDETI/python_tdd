class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #time and space : O(max(len(a), len(b)))
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            result.append(str(carry % 2))  
            carry = carry // 2             

        result.reverse()
        return ''.join(result)
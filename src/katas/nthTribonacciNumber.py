class Solution:
    def tribonacci(self, n: int) -> int:
        #time and space : O(n) and O(1)
        if n == 0:
            return 0
        if n ==1 or n==2:
            return 1
        
        a, b, c = 0,1,1
        for i in range(3,n +1):
            next = a + b +c 
            a = b
            b = c
            c = next 
        return c
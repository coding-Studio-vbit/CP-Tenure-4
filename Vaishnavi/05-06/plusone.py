def plusOne(self, digits: List[int]) -> List[int]:
        temp = digits.pop()
        temp1 = temp + 1
        num = 0
        if temp1 == 10:
            digits.append(temp)
            for i in digits:
                num = (num*10) + i
            num = num + 1
            digits = list(str(num))
        else:
            digits.append(temp1)
        return digits
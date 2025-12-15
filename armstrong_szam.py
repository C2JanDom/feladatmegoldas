import unittest

print("Input: ", end="")  
szam = (int(input()))

def armstrong_szam(num):
    num_str = str(num)
    n = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** n

    return total == num

print(f'Return: {armstrong_szam(szam)}')  

class TesztSzamok(unittest.TestCase):

    def test_153(self):
        self.assertTrue(armstrong_szam(153))

unittest.main()

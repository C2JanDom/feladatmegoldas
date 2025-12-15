import unittest

print("Input: ", end="")  
maganhangzosSzoveg = (str(input()))

def maganhangzot_torol(szoveg):
    maganhangzok = "aeiouAEIOU"
    return ''.join([char for char in szoveg if char not in maganhangzok])

print(f'Return: {maganhangzot_torol(maganhangzosSzoveg)}')

class TesztSzamok(unittest.TestCase):

    def test_szoveg(self):
        self.assertEqual(maganhangzosSzoveg('Iden Java szigeten voltunk nyaralni. Nem is tudtam, hogy elneveztek egy helyet egy programozasi nyelvrol.'), 'dn Jv szgtn vltnk nyrln. Nm s tdtm, hgy lnvztk gy hlyt gy prgrmzs nylvrl.')

unittest.main()
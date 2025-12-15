import unittest

print("Input: ", end="")  
mozgas = (str(input()))

def elmozdulas(utvonal):
    x, y = 0, 0  # Kezdetben a kiinduló pozíció (0, 0)

    for mozgás in utvonal:
        if mozgás == 'F':
            y += 1  # Felfelé mozgunk
        elif mozgás == 'L':
            y -= 1  # Lefelé mozgunk
        elif mozgás == 'J':
            x += 1  # Jobbra mozgunk
        elif mozgás == 'B':
            x -= 1  # Balra mozgunk

    # Ha nem mozdultunk el a kiinduló pozícióhoz képest
    if x == 0 and y == 0:
        return "Nem mentünk sehova"
    
    vizszintSzoveg = ""
    fuggolegesSzoveg = ""

    if x < 0:
        vizszintSzoveg = "balra"

    if x > 0:
        vizszintSzoveg = "jobbra"

    if y < 0:
        fuggolegesSzoveg = "le"

    if y > 0:
        fuggolegesSzoveg = "fel"

    return f"{x} lépés {vizszintSzoveg}, {y} lépés {fuggolegesSzoveg}"

print(f'Return: {elmozdulas(mozgas)}')

class TesztSzamok(unittest.TestCase):

    def test_jelszo(self):
        fgv = elmozdulas('FBLLLJLLJ')
        self.assertEqual(fgv, 5)

unittest.main()
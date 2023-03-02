assert 10 > 5

try:
    assert 10>20
except:
    print("Hei på deg")







def areal(hoyde, bredde):
    areal = hoyde*bredde
    return areal

def omkrets(hoyde, bredde):
    return hoyde + hoyde + bredde + bredde


assert areal(3,2) == 6
assert areal(0,1) == 0
assert areal(5,10) == 50
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14





print("koden er ferdig")
# Vern mot kjøretidsfeil og logiske feil i progammer

## Kjøretidsfeil 

Håndtering av kjøretidsfeil gjøres med nøkkelordene try og except i python
Python forsøker å kjøre kodeblokken som ligger under `try`, hvis python får en feilmelding, vil den kjøre kodeblokken som ligger under `except`.


```python

try:    
    alder = int(input("Alder: "))    
    fødselsår = 2022 - alder    
    print(f"fødselsår: {fødselsår}")

except:    
    print("feil: alder må være et heltall")print("koden fortsetter")

```

### Eksperttips: While-løkke med try-except

```python

while True:
    try:
        alder = int(input("fødselsår: "))
        break

    except:
        print("feil, alder må være et heltall")
fødselsår = 2022-alder
print(f"fødselsår = {fødselsår}")
```

## Logiske feil i programmer

For å oppdage logiske feil i programmer kan vi bruke `assert` for å forsikre oss om at koden gir korrekte resultat

Eksempel:

```python
assert 10 > 5 #gir ikke feil
assert 10>20 #gir feil
```

Eksempel test av funksjoner med assert:

```python

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


```

### Eksperttips: håntering av kjøretidsfeil og logiske feil

```python
while True:
    try:
        alder = int(input("fødselsår: "))
        assert alder <= 0
        break

    except:
        print("feil, alder må være et positivt heltall")
fødselsår = 2022-alder
print(f"fødselsår = {fødselsår}")
```
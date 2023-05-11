# Gjenbrukbar kode

Gjenbrukbar kode er kode som inneholder dokumentasjon. Som i eksempelet under vil bruken av docstrings gjøre det lettere for den som leser koden å forstå hva klassen gjør. Koden kan derfor lett brukes i ettertid og lett forstås av andre. 

## Eksempel

```python
class Pokemon:
    """
    
    Attributes:
        navn: en string med navnet til pokemon-en
        type: en string med typen til pokemonen
        helsepoeng: en int med hvor mye liv pokemonen har
        angrep: en int med hvor god pokemonen er i angrep 
        forsvar: en int med hvor god pokemonen er i forsvar

    """
    def __init__(self, navn, type, helsepoeng, angrep, forsvar):
        self._navn = navn
        self._type = type
        self._helsepoeng = helsepoeng
        self._angrep = angrep
        self._forsvar = forsvar
```


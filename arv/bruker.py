class Bruker:
    """Superklasse for brukere i skolesystemet. Skal ikke brukes direkte
    
    Attributes:
        epost: en string med brukers epost
        fornavn: en string med brukers fornavn
        etternavn: en string med brukers etternavn

    """
    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn

    def logg_inn(self):
        print(f"{self._epost} logget inn")
    
    def logg_ut(self):
        print(f"{self._epost} logget ut")

class Lærer(Bruker):
    """Subklasse for lærere i skolesystemet
    
    Attributes:
        epost: en str med lærerens epost
        fornavn: en str med lærerens fornavn
        etternavn: en str med lærerens etternavn
        lonnskonto: en str med lærerens lønnskonto
    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto):
        super().__init__(epost, fornavn, etternavn)
        self._lonnskonto = lonnskonto


class Faglærer(Lærer):
    """Subklasse for lærere i skolesystemet
    
    Attributes:
        epost: en str med lærerens epost
        fornavn: en str med lærerens fornavn
        etternavn: en str med lærerens etternavn
        lonnskonto: en str med lærerens lønnskonto
    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto):
        super().__init__(epost, fornavn, etternavn, lonnskonto)
        self._kompetanse = []
        self._klasser = []

class Kontaktlærer(Lærer):
    """Subklasse for lærere i skolesystemet
    
    Attributes:
        epost: en str med lærerens epost
        fornavn: en str med lærerens fornavn
        etternavn: en str med lærerens etternavn
        lonnskonto: en str med lærerens lønnskonto
        klasse: en str med lærerens klasse
        trinn: en str med lærerens trinn
    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lonnskonto)
        self._klasse = klasse
        self._trinn = trinn

class Elev(Bruker):
    """Subklasse for lærere i skolesystemet
    
    Attributes:
        epost: en str med elevens epost
        fornavn: en str med elevens fornavn
        etternavn: en str med elevens etternavn
        trinn: en str med elevens trinn
        klasse: en str med elevens klasse
    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse):
        super().__init__(epost, fornavn, etternavn)
        self._trinn = trinn
        self._klasse = klasse
        self._fag = []

# Denne brukes for testing, betyr at koden innenfor if-setningen
# kun kjøres hvis vi trykker play på denne filen eller kjører denne filen i terminalen
if __name__ == "__main__":
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 97003405654)
    ravi.logg_inn()
    ravi.logg_ut()

    camilla = Elev("camillac@kkg.no", "Camilla", "Coward", 2, "STG")
    camilla.logg_inn()
    camilla.logg_ut()
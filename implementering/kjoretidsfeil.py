

while True:
    try:
        alder = int(input("fødselsår: "))
        assert alder <= 0
        break

    except:
        print("feil, alder må være et heltall")
fødselsår = 2022-alder
print(f"fødselsår = {fødselsår}")

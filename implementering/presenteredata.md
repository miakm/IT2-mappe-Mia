# Presentere data

Med data mener vi all mulig informasjon, det kan f.eks. være temperatur, tekst, bilder, filmer
I IT2 lærer vi om to forskjellige måter å presentere data på, nemlig ved tegning av grafer og med nettsider

### Tegne grafer

For å tegne grafer i Python kan vi bruke biblioteket 'matplotlib'.

> Installere matplotlib: 'pip3 install matplotlib'

### Lage nettsider (HTML/flask)


## Eksempel

```python

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

plt.plot(x,y) #Oppretter et plot
#plt.show()  #Viser plottet


# x1 = [0, 1, 3, 4, 5]
# y1 = [2, 5, 11, 14, 17]

# plt.plot(x1, y1)
# plt.show()


x1 = [0, 1, 2, 3, 4, 5]
y1 = []
for tall in x1:
    y1.append(3*tall + 2)
plt.plot(x1,y1) # plot gjør at det blir en linjeplt.scatter(x1,y1) # scatter gjør at det blir punkterplt.show()
plt.scatter(x1,y1) # scatter gjør at det blir punkterplt.show()
plt.show()

```

## Bruk i større programmer
- [Enkel plotting](plotting.ipynb)
- [Plotting med funksjon](plotting-notat.ipynb)

tup = (2,3,5,6
       ,7,"Lambo")
tempo = list(tup)
tempo.append("Porsche")
tempo.insert(2,56)
tup = tuple(tempo)
print(tup.count(7))
print(tup)

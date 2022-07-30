from collections import namedtuple

dates= namedtuple('dates', "name age work")

Miguel = dates("Miguel", 15, "student")
Ana= dates('Ana', 30, 'businesswoman')

print("names:")
print(Miguel.name," ",Ana.name)
print("\n")
print("ages:")
print(Miguel.age," ",Ana.age)
print('\n')
print("works:")
print(Miguel.work," ",Ana.work)

print(dates._fields)

occupations=namedtuple('occupations',"status level")
Paulodates = ("Paulo", 47,  occupations("chef Engineer", "high"))
Paulo = dates._make(Paulodates)


print(Paulo._asdict())

print("\n")

for keys, itens in Paulo._asdict().items():
    print(keys, ":", itens)

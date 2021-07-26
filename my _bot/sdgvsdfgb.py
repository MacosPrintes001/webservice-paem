"""m={
    1:"CORI",
    2:"CJUR",
    3:"CMON"
}

print("1 - CORI\n2 - CJUR\n3 - CMON")

v=int(input("Escolha seu Campus: "))

if v in m.keys():
    print(m[v])"""


v = int(input("L: "))

if v == "1":
    v = "um"
else:
    v = "dois"

print(v)
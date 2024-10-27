"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
some examples of universe sets
"""
from NS.pyns.ns_universe import NSuniverse
# from ..pyns.ns_universe import NSuniverse

U = NSuniverse("1", 2, 3, "4", "5")
U = NSuniverse("1,2;3,4;5")
U = NSuniverse("1",2,"3",4,"5")

U.storeName()
print(f"{U:l}")

# print(repr(U))

U2 = NSuniverse([2,4,6,8])
#U2 = NSuniverse([2,4,6,8,2]) # fornisce errore perché ci sono elementi ripetuti
U2 = NSuniverse((2,4,6,8))
#U2 = NSuniverse((2,4,6,8,2)) # fornisce errore perché ci sono elementi ripetuti
U2 = NSuniverse("2,4,6,8")
# U2 = NSuniverse("2,4,6,8,2") # fornisce errore perché ci sono elementi ripetuti
#--------
#U2 = NSuniverse({2,4,6,8}) # fornisce errore perché il tipo insieme non è ammesso

U2.storeName()
print(f"{U2:l}")

V = NSuniverse(3,5,7,9)
print(V)

V2 = NSuniverse((2,4,5))
print(V2)

V3 = NSuniverse(V2)
print(V3)
print(f"{V2==V3} ?")
Z = NSuniverse("a")
print(Z)

T = NSuniverse(" ( a b c , d ; e )")
T = NSuniverse(" { a b c , d ; e }")
T = NSuniverse(" [ a b c , d ; e ]")
T.storeName()
print(f"{T:l}")
print(f"Cardinality of T is è {T.cardinality()}")
"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
disjoint neutrosophic sets
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset

U = NSuniverse(1,2,3)
A = NSset(U)
A.setElement(1,(0.4,0.3,0.4))
A.setElement(2,(0.2,0.2,1))
A.setElement(3,(0.1,0.1,0.9))
print("A =",A)

B = NSset(U)
B.setElement(1,(0.7,0.3,0.1))
B.setElement(2,(0.4,0.6,0.8))
B.setElement(3,(0.2,0.2,0.9))
print("B =",B)

C = A.NScomplement()
print("A^c =", C)

print(f"A disgiunto B = {A.isNSdisjoint(B)}")

D = A.NSintersection(C)
print("A \cap A^c =", D)

print(f"A disgiunto C = {A.isNSdisjoint(C)}")

E = NSset(U)
E.setElement(1,(0,0,1))
E.setElement(2,(0,0,0.8))
E.setElement(3,(0,0,1))

print(f"A disgiunto E = {A.isNSdisjoint(E)}")


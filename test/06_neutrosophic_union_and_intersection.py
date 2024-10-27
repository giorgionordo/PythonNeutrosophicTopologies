"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
neutrosophic union and neutrosophic intersection
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset

U = NSuniverse(1,2,3)
A = NSset(U)
A.setElement(1,(0.4,0.3,0.4))
A.setElement(2,(0.2,0.2,1))
A.setElement(3,(0.1,0.1,0.9))
print(A)

B = NSset(U)
B.setElement(1,(0.7,0.3,0.1))
B.setElement(2,(0.4,0.6,0.8))
B.setElement(3,(0.2,0.2,0.9))
print("B=\n",B)

D = NSset("a,b,c","(0.1,0.2,0.3), (0.4,0.5,0.6), (0.7,0.8,0.9)")
print("D = ",D)
#print("A unione D = ", A+D)   # unione tra insiemi neutrosofici definiti su universi differenti: NON ACCETTATA

C = A.NSunion(B)
print(f"unione = {C}")
print(f"unione = {A + B}")   # con l'overloading degli operatori

D = A.NSintersection(B)
print(f"intersezione = {D}")
print(f"intersezione = {A & B}")  # con l'overloading degli operatori

print(D.getUniverse())


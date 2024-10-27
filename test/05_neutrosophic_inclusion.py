"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
neutrosophic subsets
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

print(A.isNSsubset(B))
print(A<=B)

print(B.isNSsuperset(A))
print(B>=A)

C = NSset(B)
print(f"C =\n{C}")

print(f"B = C ?  {B==C}")
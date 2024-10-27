"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
obtain a neutrosophic toplogy generated by a base or a subbase
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_family import NSfamily

# U = NSuniverse("a,b,c")
# # U.storeName()
#
# A1 = NSset(U, "(0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)")
# A2 = NSset(U, "(0.1,0.2,0.9), (0.9,0.1,0.3), (0.5,0.3,0.4)")
# A3 = NSset(U, "(0.7,0.3,0.1), (0.8,0.4,0.0), (0.1,0.1,0.9)")
# # A3 = A1 & A2
#
# A1.storeName()
# A2.storeName()
# A3.storeName()
#
# L = NSfamily(A1, A2, A3)
# # L = NSfamily(A1, A2, A1 & A2)
# # L = NSfamily(A1, A1 & A2)
# # L = NSfamily(A1 & A2, A3)
# # L = NSfamily(A1 & A3, A2 & A3)
# # L = NSfamily(A1, A2)
# # L = NSfamily(A1,A1,A2)
# L.storeName()
# print(f"La famiglia di partenza è:\n {L:tl}")
#
# B = L.getNSBase()
# B.storeName()
# print(f"la base ha cardinalità {B.cardinality()} ed è:\n {B:tl}")
#
# T = B.getNSTopologyByBase()
# T.storeName()
# print(f"la topologia ha cardinalità {T.cardinality()} ed è:\n {T:tlx}")

#------------------------------------------------------

V2 = NSuniverse("a,b,c")
V2.storeName()
print(f"l'universo è {V2:l}")

A1 = NSset(V2, [(0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)])
A2 = NSset(V2, [(0.1,0.2,0.9), (0.9,0.1,0.3), (0.5,0.3,0.4)])
A1.storeName()
A2.storeName()

W = NSfamily(A1, A2)
W.storeName()
print(f"la famiglia sull'universo {W.getUniverse():l} è {W:lx}")

S = W.getNSBase()
S.storeName()
print(f"la base sull'universo {S.getUniverse():l} è {S:lx}")

T = W.getNSTopologyBySubBase()
T.storeName()
print(f"la topologia sull'universo {T.getUniverse():l} ha cardinalità {T.cardinality()} ed è\n{T:lx}")

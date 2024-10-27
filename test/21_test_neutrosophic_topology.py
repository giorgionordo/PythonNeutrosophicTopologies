"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
test if a family of neutrosophic sets is a neutrosophic topology
"""
from http.cookiejar import debug

from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_family import NSfamily

U = NSuniverse("a,b,c")
A1 = NSset(U, "(0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)")
A2 = NSset(U, "(0.1,0.2,0.9), (0.9,0.1,0.3), (0.5,0.3,0.4)")
A3 = NSset(U, "(0.7,0.3,0.1), (0.8,0.4,0.0), (0.1,0.1,0.9)")
# A3 = A1 & A2

A1.storeName()
A2.storeName()
A3.storeName()

L = NSfamily(A1, A2, A3)
# L = NSfamily(A1, A2, A1 & A2)
# L = NSfamily(A1, A1 & A2)
# L = NSfamily(A1 & A2, A3)
# L = NSfamily(A1 & A3, A2 & A3)
# L = NSfamily(A1, A2)
# L = NSfamily(A1,A1,A2)
L.storeName()
print(f"La famiglia di partenza è:\n {L:lx}")

# T = L.getNSBase()
T = L.getNSTopologyBySubBase()
T.storeName()

print(f"la topologia ha cardinalità {T.cardinality()} ed è:\n {T:lx}")

# print(f"E' chiusa rispetto all'unione => {T.NSunionClosed(trace=True,timereport=True)}")

# print(f"E' chiusa rispetto all'intersezione => {T.NSintersectionClosed(timereport=True)}")

# print(f"E' una topologia neutrosofica => {T.isNeutrosophicTopology(timereport=True)}")


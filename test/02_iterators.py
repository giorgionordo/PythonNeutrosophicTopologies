"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
using iterators on NSuniverse objects
"""
from NS.pyns.ns_universe import NSuniverse

U = NSuniverse(" ( a b c , d ; e )")

for i, u in enumerate(U):
    print(f"- the {i}-th element is {u}")
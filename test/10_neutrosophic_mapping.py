"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
neutrosophic mapping
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset
from NS.pyns.ns_mapping import NSmapping

U = NSuniverse("a,b,c")
V = NSuniverse(1,2)

# f = NSmapping(U, V, (2,1,2))  # funzione con values assegnati
# print("f =", f)
# print("dominio = ", f.getDomain())
# print("codominio = ", f.getCodomain())

# h = NSmapping(U,V, (2,1,2))
# h = NSmapping(U,V, [2,1,2])
# h = NSmapping(U,V, "2,1,2")
# h = NSmapping({'a':2, 'b':1, 'c':2})   # funzione definita come dizionario
# h = NSmapping("'a':2, 'b':1, 'c':2")  # funzione definita come stringa che rappresenta un dizionario
# h = NSmapping("'a'->2, 'b'->1, 'c'->2") # funzione definita come elenco di corrispondenze con le frecce ->
# h = NSmapping("'a'->2; 'b'->1; 'c'->2") # funzione definita come elenco di corrispondenze con le frecce
# h = NSmapping("('a'->2); ('b'->1); ('c'->2") # funzione definita come elenco di corrispondenze con frecce e parentesi
# h = NSmapping("'a'->2 'b'->1 'c'->2") # funzione definita come elenco di corrispondenze con le frecce e spazi senza virgole
# h = NSmapping("a->2  b->1  c->2")   # con le freccette e senza apici
# h = NSmapping("a|->2  b|->1  c|->2}")   # con le frecce "maps to"
# h = NSmapping("'a'->2  b->1  c->2")   # con le freccette e una sola coppia di apici
# h = NSmapping("{a->2  b->1  c->2}")   # con le freccette e senza apici e le graffe
# h = NSmapping("'a'->2, b|->1; (c->2)")  # in forma mista
#----
# h = NSmapping(U, V, "a->2  b->1  c->2")   # con dominio, codominio e le freccette
# h = NSmapping(U, V, "'a'->2, b|->1; (c->2)")   # con dominio, codominio e in forma mista

h = NSmapping("a,b,c", "1,2", "c->2, a->2, b->1")  # in forma disordinata

#--------- ERRORI
# h = NSmapping("a,b,c,d", V, "a->2  b->1  c->2")   # con dominio, codominio e le freccette
# h = NSmapping({'a':1, 'b':2, 'a':2})  # dizionario errato con chiave ripetuta (viene preso l'ultimo valore)
# h = NSmapping("a->1, b->2, a->2")  # dizionario esteso con chiave ripetuta (viene preso l'ultimo valore)
# h = NSmapping(U, V, "a->2  b->1  d->2")   # con dominio sbagliato
# h = NSmapping(U, V, "a->2  b->1  c->3")   # con codominio sbagliato
# h = NSmapping("qualunque cosa")

h.storeName()      # memorizza il nome dell'oggetto funzione neutrosofica nell'oggetto stesso
print(f"{h:l}")    # stampa con specificatore di formattazione per il nome dell'etichetta

print("  dominio = ", h.getDomain())
print("codominio = ", h.getCodomain())



# print(f"f = h ? {f==h}")
#
# l = NSmapping(f)  # definita come oggetto funzione
# print(f"l = {l}")

from .ns_universe import NSuniverse
from .ns_set import NSset
#--
from .ns_util import NSreplace, NSstringToDict, NSisExtDict, nameToBB, isBB
import inspect
from itertools import combinations
from functools import reduce
from time import time

class NSfamily:
    """
    Package Python Neutrosophic Sets (PYNS)
    ns_mapping.py
    Class that defines a mapping between two universes of neutrosophic sets
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, *args):
        """
        Generic constructor of a family o neutrosophic sets defined over a some universe
        or copied by another object neutrosophic family.
        ----
        Parameters:
        - args: generic argument which can be an element referable a neutrosophic set
        """
        neutrosophicfamily = list()    # lista che contiene gli oggetti insiemi neutrosofici
        #--------------------
        length = len(args)
        if length == 0:
            # crea una famiglia vuota
            universe = None
            # raise IndexError("the family must contain at least a neutrosophic set")
        elif length == 1:  # singolo insieme neutrosofico, lista, tupla oppure un oggetto famiglia neutrosofica
            elem = args[0]
            if type(elem) == NSset:   #---- singolo oggetto insieme neutrosofico
                neutrosophicfamily = [elem]
                universe = elem.getUniverse()
            elif type(elem) in [list ,tuple]: #---- lista o tupla di oggetti insiemi neutrosofici
                for e in elem:
                    if e not in neutrosophicfamily:   # evita di inserire elementi duplicati
                        e.setName(e.getName())   # per poter conservare il nome nella famiglia
                        neutrosophicfamily.append(e)
                if len(neutrosophicfamily) > 0:  # se c'è almeno un insieme neutrosofico prendi l'universo
                    universe = neutrosophicfamily[0].getUniverse()
                else:
                    universe = None
        elif length > 1:  # elenco diretto di insiemi neutrosofici
            for e in args:
                if e not in neutrosophicfamily:  # evita di inserire elementi duplicati
                    e.setName(e.getName())  # per poter conservare il nome nella famiglia
                    neutrosophicfamily.append(e)
            universe = args[0].getUniverse()
        # memorizza i valori ottenuti nelle proprietà dell'oggetto
        self.__universe = universe
        self.__neutrosophicfamily = neutrosophicfamily
        self.__name = None


    # metodo che memorizza il nome della famiglia di insiemi neutrosofici come proprietà dell'oggetto stesso
    def storeName(self):
        """
        method that stores the name of the object neutrosophic set as a property of the object itself
        """
        frame = inspect.currentframe().f_back  # ottieni il frame chiamante
        local_vars = frame.f_locals   # ottieni le variabili locali del frame chiamante
        var_name = next((nome for nome, valore in local_vars.items() if valore is self), None)
        self.__name = var_name

    #-----------

    # metodo che restituisce il nome  della famiglia di insiemi neutrosofici (se memorizzato)
    def getName(self):
        """
        method that returns the name of the object neutrosophic set (if stored), otherwise returns None
        """
        return self.__name

    #---------

    # metodo che restituisce l'universo degli insiemi neutrosifici della famiglia come oggetto NSuniverse
    def getUniverse(self):
        """
        Method that returns the universe of the neutrosophic set as object NSuniverse
        """
        return self.__universe

    #-----

    # Metodo che imposta l'universo degli insiemi neutrosofici della famiglia come oggetto NSuniverse
    def setUniverse(self, universe):
        """
        Method that sets the universe of the neutrosophic set family as an NSuniverse object,
        preserving the name if available.
        """
        if type(universe) != NSuniverse:
            raise ValueError("The universe must be an instance of NSuniverse.")
        self.__universe = universe


    #------------------------------------------------------------------------------------


    # Ridefinizione dell'operatore "in" sovrascrivendo il metodo __contains__
    def __contains__(self, nsset):
        # Verifica se nsset è presente nella famiglia
        return nsset in self.__neutrosophicfamily


    #------------------------------------------------------------------------------------

    # Metodo per rendere la classe iterabile
    def __iter__(self):
        """
        Method that returns an iterator over the neutrosophic sets in the family
        ----
        Returns: an iterator for the neutrosophic sets in the family
        """
        return iter(self.__neutrosophicfamily)

    #------------------------------------------------------------------------------------

    # metodo che restituisce la cardinalità (il numero di elementi) della famiglia di insiemi neutrosofici
    def cardinality(self):
        """
        Method that returns the cardinality (the number of elements) of the neutrosophic family
        ----
        Returns: the number of elements of the current family of neutrosophic sets
        """
        return len(self.__neutrosophicfamily)

    #------------------------------------------------------------------------------------

    # metodo che restituisce la base topologica neutrosofica ottenuta da una famiglia di insiemi neutrosofici
    # come insieme di tutte le possibili intersezioni neutrosofiche
    def getNSBase(self):
        """
        Returns the neutrosophic topological basis obtained from a family of neutrosophic sets
        (i.e. a subbase) as the set of all possible neutrosophic intersections
        """
        subbase = self.__neutrosophicfamily   # famiglia finita di insiemi neutrosofici
        base = list()   # lista che conterrà la base corrispondente
        # considero tutte le combinazioni di sottoinsiemi della sottobase
        for i in range(1, len(subbase) + 1):
            for combin in combinations(subbase, i):  # combination è la lista che contiene una sottofamiglia di insiemi neutrosofici
                # calcolo l'intersezione dei sottoinsiemi in combinazione usando il metodo di ordine superiore reduce
                intersez = reduce(lambda x, y: x.NSintersection(y), combin)
                # crea il nome per l'intersezione combinando i nomi degli insiemi nella combinazione
                names = [s.getName() for s in combin if s.getName()]  # ottieni i nomi di ogni insieme della combinazione
                intersez_name = " ∩ ".join(names) if names else None  # Unisci i nomi con " ∩ "
                if intersez_name:
                    intersez.setName(intersez_name)  # assegna il nome all'intersezione
                # controlla se questo elemento corrisponde a qualche elemento presente ed etichettato
                for s in subbase:
                    if intersez == s:
                        intersez.setName(s.getName())
                        break
                # aggiungo l'elemento alla base
                base.append(intersez)
        # converto la base in oggetto NSfamily e la restituisco
        base = NSfamily(base)
        base.setUniverse(self.getUniverse())    # mantieni l'universo col relativo nome
        return base

    #------------------------------------------------------------------------------------

    # metodo che restituisce la topologia neutrosofica ottenuta da una base neutrosofica
    # come insieme di tutte le possibili unioni neutrosofiche
    def getNSTopologyByBase(self):
        """
        Returns the neutrosophic topology obtained from a neutrosophic base
        as the set of all possible neutrosophic unions
        """
        base = self.__neutrosophicfamily   # famiglia finita di insiemi neutrosofici
        topology = list()               # lista che conterrà la base corrispondente
        universe = self.__universe
        empty = NSset.EMPTY(universe)
        empty.setName("\u2205\u0303")   # vuoto con tilde - empty.setName("∅")
        topology.append(empty)  # aggiungi l'insieme neutrosofico vuoto
        # aggiungi tutte le possibili unioni finite di sottoinsiemi della base
        for i in range(1, len(base) + 1):
            for combin in combinations(base, i):
                union = reduce(lambda x, y: x.NSunion(y), combin)
                # crea il nome per l'unione combinando i nomi degli insiemi nella combinazione
                names = [s.getName() for s in combin if s.getName()]  # Ottieni i nomi di ogni insieme nella combinazione
                # aggiungi parentesi solo se ci sono più nomi coinvolti nell'intersezione
                if len(names) > 1:
                    union_name = " ∪ ".join(f"({name})" if "∩" in name else name for name in names)
                else:
                    union_name = " ∪ ".join(names)  # Lascia senza parentesi se c'è un singolo nome
                if union_name:
                    union.setName(union_name)  # Assegna il nome all'unione
                # controlla se questo elemento corrisponde a qualche elemento presente ed etichettato
                for b in base:
                    if union == b:
                        union.setName(b.getName())
                        break
                topology.append(union)
        # Imposta il nome dell'insieme assoluto utilizzando il nome dell'universo
        absolute = NSset.ABSOLUTE(universe)
        #----- gestione del nome dell'universo
        universe_name = universe.getName()
        if isBB(universe_name) == False:    # se ha già la tilde lascialo immutato
            absolute.setName(nameToBB(universe_name) if universe_name else "\U0001D54C\u0303")
        else:
            absolute.setName(universe_name)
        topology.append(absolute)  # aggiungi l'insieme neutrosofico assoluto
        # converto la lista topologia in oggetto NSfamily e la restituisco
        topology = NSfamily(topology)
        topology.setUniverse(self.getUniverse())  # mantieni l'universo col relativo nome
        return topology

    #------------------------------------------------------------------------------------

    # metodo che restituisce la topologia neutrosofica ottenuta da una sottobase neutrosofica
    # come insieme di tutte le possibili unioni neutrosofiche di intersezioni neutrosofiche
    # di una qualunque famiglia di insiemi neutrosofici
    def getNSTopologyBySubBase(self):
        """
        Returns the neutrosophic topology obtained from a neutrosophic subbase
        as a set of all possible neutrosophic unions of neutrosophic intersections
        of any family of neutrosophic sets
        """
        nsbase = self.getNSBase()
        nstopology = nsbase.getNSTopologyByBase()
        return nstopology


    #------------------------------------------------------------------------------------

    # funzione privata generico per la visualizzazione del report sui tempi
    def __time_report(self, operation_name, start_time, success=True):
        """
        Generates a time report based on the start time and the end time.
        operation_name: The name of the operation being reported.
        start_time: The initial time when the operation started.
        success: Boolean indicating whether the operation was successful (True) or failed (False).
        """
        end_time = time()
        execution_time = end_time - start_time
        hours, remainder = divmod(execution_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        status = "positive" if success else "negative"
        print(f"Verification of closure under neutrosophic {operation_name} was {status} and lasted {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds")

    #-------------------------------------------------------------


    # Metodo privato generico per la verifica della chiusura di una famiglia neutrosofica rispetto a un'operazione
    def __check_closure(self, operation, operation_name, trace=False, timereport=False):
        """
        Generic method that checks if the neutrosophic family is closed under a given operation (union or intersection).
        The operation should be passed as a lambda function, and the operation_name should describe it for debugging purposes.
        """
        family = self.__neutrosophicfamily  # Ottieni la famiglia di insiemi neutrosofici
        l = len(family)  # Lunghezza della famiglia
        if trace:
            nmax = 2 ** l - l - 1  # Numero di sottoinsiemi con almeno due elementi
            cifremax = len(str(nmax))
            k = 0
        if timereport:
            start_time = time()
        # Consideriamo tutte le combinazioni di sottoinsiemi della famiglia
        for i in range(2, l + 1):  # Evita operazioni con meno di due insiemi
            for combin in combinations(family, i):
                if trace:
                    k += 1
                    print(f"Closure under neutrosophic {operation_name}: step {k:{cifremax}} / {nmax}")
                # Calcola l'operazione (unione o intersezione) sui sottoinsiemi nella combinazione
                result = reduce(operation, combin)
                # Controlla se il risultato è presente nella famiglia
                if result not in family:
                    if timereport:
                        self.__time_report(operation_name, start_time, success=False)
                    return False  # Se trovi un risultato non presente nella famiglia, restituisci False
        if timereport:
            self.__time_report(operation_name, start_time, success=True)
        return True  # Se tutte le combinazioni sono presenti, la famiglia è chiusa rispetto all'operazione


    #-------------------------------------------------------------


    # Metodo per verificare la chiusura rispetto all'unione
    def NSunionClosed(self, trace=False, timereport=False):
        return self.__check_closure(lambda x, y: x.NSunion(y), "union", trace=trace, timereport=timereport)

    #-----------

    # Metodo per verificare la chiusura rispetto all'intersezione
    def NSintersectionClosed(self, trace=False, timereport=False):
        return self.__check_closure(lambda x, y: x.NSintersection(y), "intersection", trace=trace, timereport=timereport)

    #-----------

    # Metodo che verifica se una famiglia neutrosofica costituisce una topologia neutrosofica
    def isNeutrosophicTopology(self, trace=False, timereport=False):
        """
        Method that checks if the neutrosophic family satisfies the axioms of a neutrosophic topology.
        Returns True if the family constitutes a neutrosophic topology, otherwise returns False.
        """
        family = self.__neutrosophicfamily
        universe = self.__universe
        if timereport:
            start_time = time()
        # Controllo se l'insieme vuoto è presente nella famiglia
        empty = NSset.EMPTY(universe)
        if empty not in family:
            return False
        # Controllo se l'insieme universo è presente nella famiglia
        absolute = NSset.ABSOLUTE(universe)
        if absolute not in family:
            return False
        # Verifica la proprietà di chiusura rispetto all'unione
        if not self.NSunionClosed(trace=trace, timereport=timereport):
            return False
        # Verifica la proprietà di chiusura rispetto all'intersezione
        if not self.NSintersectionClosed(trace=trace, timereport=timereport):
            return False
        # Se tutti i controlli passano, la famiglia è una topologia neutrosofica
        if timereport:
            self.__time_report("topology", start_time, success=True)
        return True


    #------------------------------------------------------------------------------------

    # restituisce True se la famiglia neutrosofica corrente è contenuta in quella
    # passata come parametro
    def isSubset(self, nsfamily):
        """
        Checks if the current neutrosophic family is contained in that passed as parameter
        ----
        Parameters:
        - nsfamily: second neutrosophic family
        ----
        Returns: True if the current neutrosophic family is contained in that passed as parameter
        """
        if type(nsfamily) != NSfamily:
            raise ValueError("the parameter is not a neutrosophic family")
        if self.getUniverse() != nsfamily.getUniverse():
            raise ValueError("the two neutrosophic families cannot be defined on different universe sets")
        else:
            result = True
            for e in self.__neutrosophicfamily:
                if e not in nsfamily.__neutrosophicfamily:
                    result = False
                    break
            return result

    #----------

    # operatore sottoinsieme (<=) con overloading sul metodo __le__
    def __le__(self, nsfamily):
        """ subset of neutrosophic family
        """
        if type(nsfamily) != NSfamily:
            raise ValueError("the second argument is not a neutrosophic family")
        return self.isSubset(nsfamily)

    #---------------------------------------------

    # restituisce True se la famiglia neutrosofica corrente contiene quella
    # passata come parametro
    def isSuperset(self, nsfamily):
        """
        Checks if the current neutrosophic family contains the second one passed as parameter
        ----
        Parameters:
        - nsfamily: second neutrosophic family
        ----
        Returns: True if the current neutrosophic family contains the second one
        """
        if type(nsfamily) != NSfamily:
            raise ValueError("the parameter is not a neutrosophic family")
        if self.getUniverse() != nsfamily.getUniverse():
            raise ValueError("the two neutrosophic families cannot be defined on different universe sets")
        return nsfamily.isSubset(self)

    #----------

    # operatore sovrainsieme (>=) con overloading sul metodo __ge__
    def __ge__(self, nsfamily):
        """  superset of a neutrosophic family
        """
        if type(nsfamily) != NSfamily:
            raise ValueError("the second argument is not a neutrosophic family")
        return self.isSuperset(nsfamily)

    #-----------------------------

    # confronta due famiglie di insiemi neutrosofici col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, nsfamily):
        """ Checks if the current neutrosophic family is equal to another one.
        ----
        Parameters:
        - nsfamily: second neutrosophic family
        ----
        Returns: True if the current neutrosophic family coincides with the second one
        """
        if type(nsfamily) != NSfamily:
            raise ValueError("the second argument is not a neutrosophic family")
        if self.getUniverse() != nsfamily.getUniverse():
            raise ValueError("the two neutrosophic families cannot be defined on different universe sets")
        equal = self.isSubset(nsfamily) and nsfamily.isSubset(self)
        return equal

    #----------------------

    # confronta due famiglie di insiemi neutrosoficicol metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, nsfamily):
        """ Checks if the current neutrosophic family is different from another one.
        ----
        Parameters:
        - nsfamily: second neutrosophic family
        ----
        Returns: True if the current neutrosophic family neutrosofically is different from the second one
        """
        if type(nsfamily) != NSfamily:
            raise ValueError("the second argument is not a neutrosophic family")
        if self.getUniverse() != nsfamily.getUniverse():
            raise ValueError("the two neutrosophic families cannot be defined on different universe sets")
        different = not (self == nsfamily)
        return different

    #------------------------------------------------------------------------------------

    # unione di famiglie neutrosofiche
    def union(self, other_family):
        """
        Returns the union of the current neutrosophic family with another neutrosophic family.
        ----
        Parameters:
        - other_family: NSfamily instance representing another neutrosophic family to be united with the current one.
        ----
        Returns: NSfamily object that represents the union of the two neutrosophic families.
        """
        if not isinstance(other_family, NSfamily):
            raise ValueError("The parameter is not a neutrosophic family.")
        # Check if both families are defined on the same universe
        if self.getUniverse() != other_family.getUniverse():
            raise ValueError("The two neutrosophic families cannot be defined on different universes.")
        # Combine the families while avoiding duplicates
        combined_sets = self.__neutrosophicfamily + [s for s in other_family.__neutrosophicfamily if
                                                     s not in self.__neutrosophicfamily]
        # Create a new NSfamily from the union and return it
        return NSfamily(combined_sets)

    # operatore unione (+) con overloading sul metodo __add__
    def __add__(self, other_family):
        """ neutrosophic union of two families
        """
        if not isinstance(other_family, NSfamily):
            raise ValueError("the second argument is not a neutrosophic family")
        return self.union(other_family)

    #--------------------------------------------------------------------

    # intersezione di famiglie neutrosofiche
    def intersection(self, other_family):
        """
        Returns the intersection of the current neutrosophic family with another neutrosophic family.
        ----
        Parameters:
        - other_family: NSfamily instance representing another neutrosophic family to be intersected with the current one.
        ----
        Returns: NSfamily object that represents the intersection of the two neutrosophic families.
        """
        if not isinstance(other_family, NSfamily):
            raise ValueError("The parameter is not a neutrosophic family.")
        # Check if both families are defined on the same universe
        if self.getUniverse() != other_family.getUniverse():
            raise ValueError("The two neutrosophic families cannot be defined on different universes.")
        # Find the common sets in both families
        common_sets = [s for s in self.__neutrosophicfamily if s in other_family.__neutrosophicfamily]
        # Create a new NSfamily from the intersection and return it
        return NSfamily(common_sets)

    #----------------

    # operatore intersezione (&) con overloading sul metodo __and__
    def __and__(self, other_family):
        """ neutrosophic intersection of two families
        """
        if not isinstance(other_family, NSfamily):
            raise ValueError("the second argument is not a neutrosophic family")
        return self.intersection(other_family)

    #--------------------------------------------------------------------

    # differenza di famiglie neutrosofiche
    def difference(self, other_family):
        """
        Returns the difference of the current neutrosophic family with another neutrosophic family.
        ----
        Parameters:
        - other_family: NSfamily instance representing another neutrosophic family to subtract from the current one.
        ----
        Returns: NSfamily object that represents the difference of the two neutrosophic families.
        """
        if not isinstance(other_family, NSfamily):
            raise ValueError("The parameter is not a neutrosophic family.")
        # Check if both families are defined on the same universe
        if self.getUniverse() != other_family.getUniverse():
            raise ValueError("The two neutrosophic families cannot be defined on different universes.")
        # Trova gli insiemi presenti solo nella prima famiglia
        unique_sets = [s for s in self.__neutrosophicfamily if s not in other_family.__neutrosophicfamily]
        # Crea una nuova NSfamily con la differenza e restituiscila
        return NSfamily(unique_sets)

    #-----------------------------------

    # Overloading dell'operatore - per la differenza
    def __sub__(self, other_family):
        """ Neutrosophic difference of two families
        """
        if not isinstance(other_family, NSfamily):
            raise ValueError("The second argument is not a neutrosophic family")
        return self.difference(other_family)

    #--------------------------------------------------------------------

    # complementare di una famiglia neutrosofica
    def complement(self):
        """
        Returns the family of neutrosophic sets where each set is the complement
        of the corresponding set in the current family.
        ----
        Returns: NSfamily object containing the complementary neutrosophic sets of the current family.
        """
        complementary_sets = [ns_set.NScomplement() for ns_set in self.__neutrosophicfamily]
        return NSfamily(complementary_sets)

    #----------------

    # operatore complementare (~) con overloading sul metodo __invert__ per famiglie di insiemi neutrosofici
    def __invert__(self):
        """ Complementary family of neutrosophic sets
        """
        return self.complement()

    #------------------------------------------------------------------------------------

    # restituisce la famiglia di insiemi neutrosofici come stringa col metodo speciale __str__
    def __str__(self, tabularFormat=False, label=False, extended=False):
        """
        Method that returns the family of neutrosophic sets in string format for the user.
        ----
        Parameters:
        - tabularFormat: boolean value:
           * if false, the method returns the textual representation in simplified format
           * if true, the method returns the textual representation in tabular form
        - label: boolean value: if true add the name of the object
        - extended: boolean value:
          * if true, the representation will display at most two sets per line (only when tabularFormat=False)
        ----
        Returns: string containing a table representing the degree of membership, indeterminacy, and
                 non-membership of every element of the neutrosophic set
        """
        labelname = ""
        if label:
            if self.__name is not None:
                labelname = f"{self.__name} = "
        # Gestione del caso di famiglia vuota
        if not self.__neutrosophicfamily:
            return labelname + "\u2205"  # Rappresenta la famiglia vuota col simbolo unicode insieme vuoto
        # Se esteso e tabularFormat=False, aggiungi al massimo due insiemi per riga
        indentamento = " "*(len(labelname) + 2)
        if not tabularFormat:
            if extended:
                # Ottieni la rappresentazione testuale di ogni insieme nella famiglia con etichetta
                items = [a.__str__(tabularFormat=tabularFormat, label=True, extended=extended) for a in
                         self.__neutrosophicfamily]
                # Formatta per mettere al massimo due elementi per riga
                formatted_lines = [", ".join(items[i:i + 2]) for i in range(0, len(items), 2)]
                # Unisci le righe formattate con un a capo, aggiungendo una sola graffa all'inizio e alla fine
                return labelname + "{ " + f",\n{indentamento}".join(formatted_lines) + " }\n"
            else:
                # Se extended è False, tutti gli insiemi su una sola riga con etichetta
                return labelname + "{ " + ", ".join(
                    [a.__str__(tabularFormat=tabularFormat, label=True, extended=extended) for a in
                     self.__neutrosophicfamily]) + " }\n"
        # Se tabularFormat=True elenca gli insiemi neutrosofici come tabelle
        res = labelname + "{ " + ", ".join(
            [a.__str__(tabularFormat=tabularFormat, label=True, extended=extended) for a in
             self.__neutrosophicfamily]) + " }\n"
        return res

    #----------------------------------------

    # metodo privato per la stampa formattata
    def __format__(self, spec):
        """ Method that returns the formatted string according to a given specifier
            provided as the second parameter.
        ----
        Parameters:
        - spec: stringa di formattazione:
          * ":s" (default value) : simple format
          * ":t" : tabular format
          * ":l" : add the label with the name of the object (if available)
          * ":x" : extended space for the element and label column, i.e. the first column
        ----
        Returns: the formatted string according to the spec specifier
        """
        label = True if "l" in spec else False   # aggiungi l'etichetta
        extended = True if "x" in spec else False   # formato esteso
        if "t" in spec:    # formattazione tabulare
            result = self.__str__(tabularFormat=True, label=label, extended=extended)
        else:              # formattazione semplificata
            result = self.__str__(tabularFormat=False, label=label, extended=extended)
        return result



    # restituisce la rappresentazione della famiglia di insiemi neutrosofici come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ Method that returns the neutrosophic set in string format for other implementations
        (e.g., for use in other classes).
        ----
        Returns: a detailed representation of the current neutrosophic set
        """
        s = f"Family of neutrosophic sets: {str(self)}"
        return s
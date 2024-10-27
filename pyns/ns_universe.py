from .ns_util import NSreplace, nameToBB
import inspect

class NSuniverse:
    """
    Package Python Neutrosophic Sets (PYNS)
    ns_universe.py
    Class defining a universe set for neutrosophic sets
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, *args):
        """
        Generic constructor of a universe set which accepts list, tuple, string,
        list of af values, or other universe object.
        ----
        Parameters:
        - args: generic argument (list, tuple, string, list of values or an universe object)
        """
        universe = list()   # lista di stringhe
        #--------------------
        length = len(args)
        if length == 0:
            # universe = None
            raise IndexError("the universe set must contain at least an element")
        elif length == 1:
            elem = args[0]
            if type(elem) in [list, tuple]:
                universe = [str(e) for e in elem]
            elif type(elem) == NSuniverse:
                universe = elem.get()
            elif type(elem) == str:
                sostituz = { "{":"", "}":"", "[":"", "]":"", "(":"", ")":"",
                             ",":" ", ";":" " }
                universe = NSreplace(elem, sostituz).split()
            elif type(elem) == set:
                raise ValueError("type set is not suitable because the elements of the universe set must be assigned in a specific order")
            else:  # se si tratta di un solo elemento non di tipo stringa
                universe = [str(elem)]
        else:   # se la lunghezza è maggiore di 1
            for i in range(length):
                universe.append(str(args[i]))
        # controlla che non siano stati assegnati elementi ripetuti
        univset = set(universe)
        if len(universe) != len(univset):
            raise ValueError("the universe set cannot contain repeated elements")
        # memorizza il valore ottenuto nella proprietà dell'oggetto
        self.__universe = universe
        self.__name = None


    # ---------------------------------------------------------------

    # metodo che memorizza il nome dell'oggetto insieme universo come proprietà dell'oggetto stesso
    def storeName(self):
        """
        method that stores the name of the object universe set as a property of the object itself,
        converting it to Blackboard Bold format with a tilde.
        """
        frame = inspect.currentframe().f_back
        local_vars = frame.f_locals
        var_name = next((nome for nome, valore in local_vars.items() if valore is self), None)
        self.__name = nameToBB(var_name) if var_name else None

    # -----------

    # metodo che forza il nome (etichetta) dell'oggetto insieme universo
    def setName(self, name):
        """
        method that forces the name (label) of the object universe set
        Args:
            name: name to assign
        """
        self.__name = name

    # -----------

    # metodo che restituisce il nome dell'oggetto insieme universo (se memorizzato)
    def getName(self):
        """
        method that returns the name of the object universe set (if stored), otherwise returns None
        """
        return self.__name

    #------------------------------------------------------------------------------------

    # restituisce l'universo come lista di stringhe
    def get(self):
        """
        Method that returns the universe as a list of strings.
        ----
        Returns: list of the elements of the universe
        """
        return self.__universe


    # metodo che restituisce la cardinalità (il numero di elementi) dell'universo
    def cardinality(self):
        """
        Method that returns the cardinality (the number of elements) of the universe set
        ----
        Returns: the number of elements of the current universe set
        """
        return len(self.__universe)

    #------------------------------------------------------------------------------------

    # restituisce True se l'insieme universo corrente è contenuto in quello
    # passato come parametro
    def isSubset(self, unv):
        """
        Checks if the current universe set is contained in the second one passed as parameter.
        ----
        Parameters:
        - unv: second universe set
        ----
        Returns: True if the current universe set is contained in the second one
        """
        setself = set(self.get())
        setunv = set(unv.get())
        result = setself.issubset(setunv)
        return result

    #------------------------------------------------------------------------------------

    # confronta due insiemi universo col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, unv):
        """ Checks if the current universe is equal to another one.
        ----
        Returns: True if the universes are equal
        """
        equal = (self.get() == unv.get())
        return equal


    # confronta due insiemi universo col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, unv):
        """ Checks if the current universe is different from another one.
        ----
        Returns: True if the universes are different
        """
        different = not (self == unv)
        return different


    #------------------------------------------------------------------------------------

    #----------------- iteratore di oggetti NSuniverse

    # definisce l'iteratore per l'oggetto insieme universo azzerando l'indice
    def __iter__(self):
        """ Method that initializes iterator on elements of the current universe set
        """
        self.__i = 0   # inizializza l'indice privato __i da usare come contatore
        return self

    # restituisce il prossimo elemento iterato dell'oggetto insieme universo
    def __next__(self):
        """ Method that returns the iterated element of the current universe set
        ----
        Returns: the element of index self.__i  of the universe set
        """
        if self.__i < len(self.__universe):    # se l'indice __i non eccede la lunghezza dell'insieme universo
            elem = self.__universe[self.__i]  # preleva l'elemento di indice __i
            self.__i +=1                       # incremente il contatore privato __i
            return elem                        # e restituisce l'elemento
        raise StopIteration                    # altrimenti interrompi l'iterazione


    # ------------------------------------------------------------------------------------

    # restituisce l'universo come stringa col metodo speciale __str__
    def __str__(self, label=False):
        """ Method that returns the universe in string format for the user.
        ----
        Parameters:
        - label: boolean value to include the name label if set to True.
        ----
        Returns: string containing a list of the elements of the universe set.
        """
        labelname = f"{self.__name} = " if label and self.__name else ""
        list_string_elements = [str(e) for e in self.__universe]
        return labelname + "{ " + ", ".join(list_string_elements) + " }"

    # metodo speciale per la stampa formattata
    def __format__(self, spec):
        """ Method that returns the formatted string according to a given specifier
            provided as the second parameter.
        ----
        Parameters:
        - spec: string format specifier:
          * ":s" (default) : simple format
          * ":l" : includes the label with the name of the object, if available.
        ----
        Returns: the formatted string according to the spec specifier
        """
        label = "l" in spec  # includes label if "l" is in the spec
        return self.__str__(label=label)

    # restituisce la rappresentazione universo come stringa col metodo speciale __repr__
    def __repr__(self):
        """ Method that returns the universe in string format for other implementations.
        ----
        Returns: a detailed representation of the current universe set.
        """
        labelname = f"{self.__name} = " if self.__name else "Universe set: "
        return f"{labelname}{str(self)}"

from .ns_universe import NSuniverse
from .ns_set import NSset
#--
from .ns_util import NSreplace, NSstringToDict, NSisExtDict
import inspect

class NSmapping:
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
        Generic constructor of a mapping between two universes.
        It can be defined:
        - by assigning only the domain and the codomain and, optionally, a list of values
        - by passing another object mapping
        ----
        Parameters:
        - args: generic argument; it can be a single parameter corresponding to:
                - a dictionary element:value
                - a string with a list of correspondance element->value, or
                - an already existent object NSmapping
                or a triple of arguments representing respectively:
                - domain
                - codomain, and
                - the list of function values expressed as strings, lists or tuples
        """
        map = dict()
        #--------------------
        length = len(args)
        if length == 0:
            raise ValueError("constructor method must have at least one parameter")
        #---------- un parametro ----------------------------------------------------------------------------------
        elif length == 1:
            if type(args[0]) == NSmapping:  # se è un oggetto NSmapping lo ricopia
                domain = args[0].getDomain()
                codomain = args[0].getDomain()
                map = args[0].getMap()
            # -------------------------------------------------------
            elif type(args[0]) == dict:  # se è un dizionario
                map = args[0]
                domain = NSuniverse(list(map.keys()))
                codomain = NSuniverse(list(set(map.values())))  # elimina gli elementi ripetuti nei valori
            elif type(args[0]) == str:  # se è una stringa prova a prelevarne gli elementi conme dizionario esteso
                try:
                    map_dict = NSstringToDict(args[0])  # ottiene il dizionario dalla stringa utilizzando una funzione di utilità
                except:
                    raise ValueError("invalid parameter")
                nsmap = NSmapping(map_dict)  # crea un oggetto NSmapping utilizzando lo stesso costruttore per funzioni passando il dizionario
                # ottiene dominio, codominio e mappa dall'aggetto NSmapping
                domain = nsmap.getDomain()
                codomain = nsmap.getCodomain()
                map = nsmap.getMap()
            # -------------------------------------------------------
            else:  # altrimenti solleva una eccezione
                raise ValueError("the type of the parameter do not match those of the constructor method")
        #---------- tre parametri --------------------------------------------------------------------------------
        elif length == 3:    # devono esserci tre parametri (dominio, codominio ed elenco valori)
            # prova a convertire i primi due parametri in oggetti di tipo insieme universo
            # ed intercetta eventuali eccezioni dal costruttore di NSuniverse
            try:
                domain = NSuniverse(args[0])
            except:
                raise ValueError("the first parameter of the constructor method must be a universe set")
            #------
            try:
                codomain = NSuniverse(args[1])
            except:
                raise ValueError("the second parameter of the constructor method must be a universe set")
            # al terzo parametro facciamo corrispondere i possibili valori che devono essere compatibili col dominio ed il codominio forniti
            values = args[2]
            card_domain = domain.cardinality()   # calcola la cardinalità del dominio

            #----------- se i valori sono espressi come dizionario o in formato stringa dizionario esteso
            if type(values)==dict or NSisExtDict(values)==True:
                # ---- crea un oggetto di tipo NSmapping con lo stesso costruttore fornendo solo i valori
                # come dizionario o dizionario esteso
                nsmap = NSmapping(values)
                # ------------ effettua i controlli tra il dominio e il codominio forniti e quello dell'oggetto ottenuto
                # verifica che il dominio della funzione ottenuta e quello dato coincidano
                # (la funzione deve essere ovunque definita) altrimenti solleva una eccezione
                # si noti che occorre confrontare i due domini come insiemi semplici,
                # cioè senza tenere conto dell'ordine degli elementi
                if set(nsmap.getDomain()) != set(domain):
                    raise ValueError("the indicated domain is incompatible with the definition of the mapping")
                # verifica che il codominio della funzione ottenuta sia contenuto in quello dato
                # (l'immagine deve essere contenuta nell'insieme di arrivo) altrimenti solleva una eccezione

                if nsmap.getCodomain().isSubset(codomain) == False:
                    raise ValueError("the indicated codomain is incompatible with the definition of the mapping")
                # se invece c'è compatibilità tra domini e codomini estrai il dizionario delle corrispondenze
                map = nsmap.getMap()

            #----------- i valori sono espressi come lista o tupla anche in formato stringa
            elif type(values) in [list, tuple, str]:
                if type(values) in [list, tuple]:  # tratta il sottocaso liste o tuple
                    values = [str(e) for e in values]  # converti in lista di stringhe
                else:                    # tratta il sottocaso stringa contenente lista o tupla
                    sostituz = {"[": "", "]": "", "(": "", ")": "",
                                ",": " ", ";": " "}
                    values = NSreplace(values, sostituz).split()  # sostituisce i valori e riduce a lista
                #----------- operazioni comuni ai due casi
                # controlla che il numero di valori sia pari alla cardinalità del dominio
                if len(values) != card_domain:
                    raise IndexError("the number of values passed does not coincide with the cardinality of the declared domain")
                # controlla che tra i values non ci siano elementi estranei al codominio
                values_set = set(values)
                codomain_set = set(codomain.get())
                if not values_set.issubset(codomain_set):
                    raise ValueError("one or more values do not belong to the declared codomain")
                # procede col preparare l'associazione dei valori nel dizionario map
                # trattandosi di lista o di una tupla segue l'ordine naturale
                for i in range(card_domain):
                    map[domain.get()[i]] = values[i]

            else:   # in tutti gli altri casi solleva una eccezione
                raise ValueError("the third parameter of the constructor method must express a value match")

        # ---------- se non ci sono uno tre parametri solleva una eccezione --------------------------------------
        else:
            raise IndexError("the number of parameters do not match those of the constructor method")
        # memorizza i valori ottenuti nelle proprietà dell'oggetto
        self.__domain = domain
        self.__codomain = codomain
        self.__map = map
        self.__name = None

    #-----------------------------------

    # metodo che memorizza il nome dell'oggetto funzione neutrosofica come proprietà dell'oggetto stesso
    def storeName(self):
        """
        method that stores the name of the object neutrosophic mapping as a property of the object itself
        """
        frame = inspect.currentframe().f_back  # ottieni il frame chiamante
        local_vars = frame.f_locals   # ottieni le variabili locali del frame chiamante
        var_name = next((nome for nome, valore in local_vars.items() if valore is self), None)
        self.__name = var_name

    #-----------
    # metodo che restituisce il nome dell'oggetto funzione neutrosofica (se memorizzato)
    def getName(self):
        """
        method that returns the name of the object neutrosophic mapping (if stored), otherwise returns None
        """
        return self.__name


    # ------------------------------------------------------------------------------------

    # restituisce il dominio della funzione
    def getDomain(self):
        """ Obtain the domain of the mapping.
        ----
        Returns: the universe set corresponding to the domain of the current mapping
        """
        return NSuniverse(self.__domain.get())


    # restituisce il codominio della funzione
    def getCodomain(self):
        """ Obtain the codomain of the mapping.
        ----
        Returns: the universe set corresponding to the codomain of the current mapping
        """
        return NSuniverse(self.__codomain.get())


    # restituisce le coppie elemento-valorej come dizionario
    def getMap(self):
        """ Obtain all the element:value pair defining the mapping.
        ----
        Returns: the dictionary containing the element-value pairs of the mapping
        """
        return self.__map


    # ------------------------------------------------------------------------------------

    # assegna il valore mediante la funzione per uno specifico elemento
    def setValue(self, u, v):
        """
        Assigns a single value by the neutrosophic mapping to a specific element of the domain, i.e. f(u)=v
        ----
        Parameters:
        - u: element of the domain
        - v: element of the codomain
        """
        u = str(u)
        v = str(v)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.__domain.get():
            raise IndexError("non-existent element in the domain of the mapping")
        if v not in self.__codomain.get():
            raise IndexError("non-existent element in the codomain of the mapping")
        self.__map[u] = v


    # ------------------------------------------------------------------------------------

    # ottiene il valore mediante la funzione di un determinato elemento del dominio
    def getValue(self, u):
        """
        Get the value by the neutrosophic mapping of a specific element of the domain.
        ----
        Parameters:
        - e: element of the domain
        ----
        Returns: the value of u by the current mapping
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.__domain.get():
            raise IndexError("non-existent element in the domain of the mapping")
        return self.__map[u]


    # ------------------------------------------------------------------------------------

    # ottiene la fibra della funzione di un determinato elemento del codominio
    def getFibre(self, v):
        """
        Get the fibre (i.e. the inverse image of a singleton) by the neutrosophic mapping
        of a specific element of the codomain.
        ----
        Parameters:
        - v: element of the codomain
        ----
        Returns: the fibre of v expressed as list of elements of the domain
        """
        v = str(v)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if v not in self.__codomain.get():
            raise IndexError("non-existent element in the codomain of the mapping")
        fibre = list()
        for e in self.__map:
            if self.__map[e] == v:
                fibre.append(e)
        return fibre


    # ------------------------------------------------------------------------------------

    # restituisce l'immagine di un insieme neutrosofico mediante una funzione
    def NSimage(self, nset):
        """
        Method that returns the neutrosophic image of a neutrosophic set by a mapping.
        ----
        Parameters:
        - nset: neutrosophic set on the domain
        ----
        Returns: neutrosophic image of nset by the current mapping
        """
        result = NSset(self.__codomain)
        for v in self.getCodomain():
            fibre = self.getFibre(v)
            if fibre == []:
                triple = [1,1,0]
            else:
                mu_values = list()
                sigma_values = list()
                omega_values = list()
                for u in fibre:
                    mu_values.append(nset.getMembership(u))
                    sigma_values.append(nset.getIndeterminacy(u))
                    omega_values.append(nset.getNonMembership(u))
                triple = [max(mu_values), max(sigma_values), min(omega_values)]  # i.e. (mu, sigma, omega)
            result.setElement(v, triple)
        return result


    # restituisce la controimmagine di un insieme neutrosofico mediante una funzione
    def NScounterimage(self, nset):
        """
        Method that returns the neutrosophic counterimage of a neutrosophic set by a mapping.
        ----
        Parameters:
        - nset: neutrosophic set on the codomain
        ----
        Returns: neutrosophic counterimage of nset by the current mapping
        """
        result = NSset(self.__domain)
        for u in self.getDomain():
            value = self.getValue(u)
            triple = nset.getElement(value)   # i.e. (mu, sigma, omega)
            result.setElement(u, triple)
        return result


    # ------------------------------------------------------------------------------------


    # confronta due funzioni col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, g):
        """ Checks if the current mapping is equal to another one.
        ----
        Parameters:
        - g: second mapping
        ----
        Returns: True if the current mapping coincides with the second one
        """
        if self.getDomain() != g.getDomain() or self.getCodomain() != g.getCodomain():
            return False
        else:
            equal = True
            for e in self.getDomain():
                if self.getValue(e) != g.getValue(e):
                    equal = False
                    break
            return equal


    # confronta due funzioni col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, g):
        """ Checks if the current mapping is different from another one.
        ----
        Parameters:
        - g: second mapping
        ----
        Returns: True if the current mapping is different from the second one
        """
        different = not (self == g)
        return different


    # ------------------------------------------------------------------------------------

    # restituisce la funzione neutrosofica come stringa col metodo speciale __str__
    def __str__(self, label=False):
        """ Method that returns the mapping in string format for the user.
        ----
        Parameters:
        - label: boolean value: if true add the name of the object
        ----
        Returns: string containing a map of the current mapping
        """
        lblwidth = 8                          # larghezza del nome della funzione
        unvwidth = 20                         # larghezza in colonne del dominio e del codominio
        totwidth = unvwidth*2 + lblwidth*4   # calcolo della larghezza totale
        labelname = " "*(lblwidth+2)
        if label == True:
            if self.__name is not None:
                labelname = f"{self.__name:>{lblwidth}s} : "
        s = f"\n{labelname} {self.getDomain():>{unvwidth}}   ->   {self.getCodomain():<{unvwidth}}\n" + "-" * totwidth + "\n"
        for e in self.__domain:     # per consentire la stampa degli elementi nell'ordine definito nel dominio
            s += f" {e:>{unvwidth+lblwidth+3}}  |->  {self.__map[e]:<{unvwidth}}\n"
        return s

    # metodo privato per la stampa formattata
    def __format__(self, spec):
        """ Method that returns the formatted string according to a given specifier
            provided as the second parameter.
        ----
        Parameters:
        - spec: stringa di formattazione:
          * ":l" : add the label with the name of the object (if available)
        ----
        Returns: the formatted string according to the spec specifier
        """
        if "l" in spec:    # aggiungi l'etichetta
            label = True
        else:
            label = False
        result = self.__str__(label=label)
        return result


    # restituisce la rappresentazione funzione neutrosofica come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ Method that returns the mapping for other implementations
        (e.g., for use in other classes).
        ----
        Returns: a detailed representation of the current mapping
        """
        return f"Neutrosophic mapping: {str(self)}"


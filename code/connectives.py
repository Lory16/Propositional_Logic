"""
START: 08/03/21
CONNECTIVES
-et : 'and'
-vel : 'or'
-implies : 'imp'
-coimplies : 'co'
"""
#VARIABILI DI PROVA
A = [True, True, False, False]
B = [True, False, True, False]


#DEFINIZIONE FUNZIONI
def op_and(A, B):
    """
    FUNCTION
    It does 'A and B'
    PARAMETHERS
    - A : list of int = {0, 1}
    - B : list of int = {0, 1}
    RETURN
    list of values, resulting from the and between each value
    of A, B
    """
    res = []

    for a, b in zip(A, B):
        res.append(a and b)
    
    return res


def op_or(A, B):
    """
    FUNCTION
    It does 'A or B'
    PARAMETHERS
    - A : list of int = {0, 1}
    - B : list of int = {0, 1}
    RETURN
    list of values, resulting from the or between each value
    of A, B
    """
    res = []

    for a, b in zip(A, B):
        res.append(a or b)
    
    return res


def op_imp(A, B):
    """
    FUNCTION
    It does 'A implies B'
    PARAMETHERS
    - A : list of int = {0, 1}
    - B : list of int = {0, 1}
    RETURN
    list of values, resulting from the implication between each value
    of A, B
    """
    res = []

    for a, b in zip(A, B):
        res.append(not a or b)

    return res


def op_co(A, B):
    """
    FUNCTION
    It does 'A co-implies B'
    PARAMETHERS
    - A : list of int = {0, 1}
    - B : list of int = {0, 1}
    RETURN
    list of values, resulting from the co-implication between each value
    of A, B
    """
    res = []

    F1 = op_imp(A, B) 
    F2 = op_imp(B, A)
    for f1, f2 in zip(F1, F2):
        res.append(f1 and f2)

    return res

"""
AB = co(A, B)
print(AB)
A = 0
B = 0
print(A or B)
"""
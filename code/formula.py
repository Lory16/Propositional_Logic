"""
START: 08/03/21
TODO
---better parsing: don't impose to have variables composed of
    only one letter
"""
import re
from connectives import op_imp, op_co


class Formula(object):
    def __init__(self, formula):
        self.formula = formula
        self.variables = self.mk_var(formula)
    
    def get_formula(self):
        return self.formula

    def get_variables(self):
        return self.variables

    def print_variables(self):
        """
        Print truth table of formula's variables
        """
        i = 0
        # print variables' names
        for var in self.variables.keys():
            print(var, end = '   ')
        print('\n')
        # print truth table
        for i in range(0, 2 ** len(self.variables.keys())):
            for column in self.variables.values():
                if column[i]:
                    print(1, end = '   ')
                else:
                    print(0, end='   ')
            print('\n')

    def mk_var(self, input):
        """
        this creates a dictionary of variables with the shape:
            variable -> [list of 0s and 1s]
        """
        variables = {}
        # create a list made of all formula's capital letters
        letters = re.findall(r'[A-Z]', input)
        # put those variables as keys in a dictionary
        for var in letters:
            if var not in variables:
                variables[var] = []
        
        # bisectional method to assign 0s and 1s to each variable
        pow2 = 2 ** len(variables.keys())
        n = pow2
        for var in variables.keys():
            loop = pow2 / (n/2)

            i = 0
            # putting groups of 0s and 1s
            while i < loop:
                j = 0
                # each group is made of n/2 elements
                while j < n/2: 
                    if i % 2 == 1: # even
                        variables[var].append(False)
                    else: # odd
                        variables[var].append(True)
                    j += 1
                i += 1
            
            n = n / 2

        return variables

#VARIABILI DI PROVA
input_ex = 'A and (B or C)'
formula_ex = Formula(input_ex)
formula_ex.print_variables()